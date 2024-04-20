import os, json
from db_interface import DBInterface
from models import School, Event, Gymnast, Lineup, LineupEntry, Judge


def insert_missing_schools(db_int: DBInterface, school_names: [str]) -> [School]:
    """
    This function inserts School objects. It will only insert unique schools.
    :param db_int: The Database Interface to use.
    :param school_names: A list of school names.
    :return: A list of School objects matching the input list.
    """
    schools_in_db = db_int.get_schools_by_names(school_names)
    print(f"Found {len(schools_in_db)} schools in DB.")
    schools_to_insert = []
    for school in school_names:
        if school not in [school_from_db.school_name for school_from_db in schools_in_db]:
            schools_to_insert.append(
                School(school_name=school)
            )
        else:
            print(f"\tSchool \"{school}\" already exists.")

    db_int.insert(*schools_to_insert)

    return list(db_int.get_schools_by_names(school_names))


def convert_json_to_gymnasts(db_int, gymnasts_information) -> [Gymnast]:
    schools_in_db = {school.school_name: school for school in db_int.get_schools()}

    gymnasts: [Gymnast] = []

    for gymnast in gymnasts_information:
        school_name = gymnast["school_id"]
        if school_name not in schools_in_db:
            print(f"Couldn't find school by name {school_name} in DB.")
            continue
        gymnast_object = Gymnast(
            first_name=gymnast["first_name"],
            last_name=gymnast["last_name"],
            major=gymnast["major"],
            classification=gymnast["classification"],
            school_id=schools_in_db[school_name].school_id
        )
        gymnasts.append(gymnast_object)

        if "gymnast_picture" in gymnast:
            gymnast_object.gymnast_picture = load_image_from_file(gymnast["gymnast_picture"])

    return gymnasts


def insert_missing_gymnasts(db_int: DBInterface, gymnast_objects: [Gymnast]) -> [Gymnast]:
    """
    This function inserts Gymnasts objects. It will only add unique Gymnasts.
    :param db_int: The Database Interface to use.
    :param gymnast_objects: A list of Gymnasts objects.
    :return: A list of Gymnast objects matching the input list.
    """
    # The line below this is evil. It gets Gymnasts by name and returns tuples of their names
    gymnasts_in_db = [(gymnast.first_name, gymnast.last_name) for gymnast in db_int.get_gymnasts_by_names(
            [(gymnast.first_name, gymnast.last_name) for gymnast in gymnast_objects]
        )
    ]
    gymnasts_to_insert = []
    for gymnast in gymnast_objects:
        if (gymnast.first_name, gymnast.last_name) not in gymnasts_in_db:
            gymnasts_to_insert.append(gymnast)
        else:
            print(f"\tGymnast {gymnast.first_name} {gymnast.last_name} already in  DB.")

    db_int.insert(*gymnasts_to_insert)

    return list(db_int.get_gymnasts_by_names(
        [(gymnast.first_name, gymnast.last_name) for gymnast in gymnast_objects]
    ))


def convert_json_to_events(events_information):
    return [
        Event(
            event_name=event_info["event_name"],
            event_location=event_info["event_location"],
            event_date=event_info["event_date"]
        )
        for event_info in events_information
    ]


def insert_missing_events(db_int: DBInterface, event_information: [dict]):
    events = [event.event_name for event in db_int.get_events()]

    events_to_insert = []
    for event in event_information:
        if event["event_name"] not in events:
            events_to_insert.append(Event(**event))
        else:
            print(f"Event \"{event["event_name"]}\" already exists.")

    db_int.insert(*events_to_insert)


def insert_missing_judges(db_int: DBInterface, judge_information: [dict]):
    # Getting events so we can populate the relationships
    events = {event.event_name: event for event in db_int.get_events()}
    judges = {f"{judge.first_name} {judge.last_name}": judge for judge in db_int.get_judges()}

    judges_to_insert = []
    for judge in judge_information:
        full_name = f"{judge["first_name"]} {judge['last_name']}"
        if judge["event_id"] in events:
            if full_name in judges:
                print(f"Judge \"{full_name}\" at event \"{judge["event_id"]}\" already exists in database.")
            else:
                judge["event_id"] = events[judge["event_id"]].event_id
                judges_to_insert.append(Judge(
                    **judge
                ))
        else:
            print(f"Event \"{judge["event_id"]}\" does not exist in database.")

    db_int.insert(*judges_to_insert)

    return db_int.get_judges()


def convert_json_to_lineups_and_lineup_entries(
        db_int: DBInterface,
        lineup_information: dict
) -> ([Lineup], [LineupEntry]):
    events = {event.event_name: event for event in db_int.get_events()}
    schools = {school.school_name: school for school in db_int.get_schools()}

    lineups: [Lineup] = []
    lineup_entries: [LineupEntry] = []

    for lineup in lineup_information:
        complete_lineup = True

        if lineup["event_id"] in events and lineup["school_id"] in schools:  # Match the Lineup to the Event
            lineup["event_id"] = events[lineup["event_id"]].event_id
            lineup["school_id"] = schools[lineup["school_id"]].school_id
        else:
            complete_lineup = False

        lineup_object = Lineup(
            event_id=lineup["event_id"],
            apparatus_name=lineup["apparatus_name"],
            school_id=lineup["school_id"]
        )

        entries_for_current_lineup: [LineupEntry] = []
        for gymnast_name in lineup["gymnasts"]:
            gymnast: list[Gymnast] = db_int.get_gymnast_by_name(*gymnast_name.split(" "))
            if len(gymnast) != 1:
                print(f"No gymnast named \"{gymnast_name}\"!!!")
                complete_lineup = False
                continue
            gymnast: Gymnast = gymnast[0]

            lineup_entry = LineupEntry(
                lineup_id=lineup_object,
                gymnast_id=gymnast.gymnast_id,
                score=0.00,
                status="Incomplete"
            )
            entries_for_current_lineup.append(lineup_entry)

        if complete_lineup:
            lineups.append(lineup_object)
            lineup_entries += entries_for_current_lineup
        else:
            print(f"Could not create lineup for School Id: {lineup_object.school_id} for Event: {lineup_object.event_id}")

    return lineups, lineup_entries


def insert_missing_lineups(
        db_int: DBInterface,
        lineups: list[Lineup],
):
    lineups_to_insert: list[Lineup] = []
    for lineup in lineups:
        lineup: Lineup = lineup
        # Pull matching lineups from DB
        matching_lineups = db_int.get_lineups_by_event_and_apparatus_and_school(
            lineup.event_id,
            lineup.apparatus_name,
            lineup.school_id
        )

        if len(matching_lineups) > 0:
            print(f"Lineup {matching_lineups[0]} already exists in database.")
            continue

        lineups_to_insert.append(lineup)

    print(f"Inserting {len(lineups_to_insert)} lineups...")
    db_int.insert(*lineups_to_insert)


def insert_missing_lineup_entries(
        db_int: DBInterface,
        lineup_entries: list[LineupEntry]
):
    lineup_entries_to_insert: list[LineupEntry] = []
    for lineup_entry in lineup_entries:
        lineup: Lineup = lineup_entry.lineup_id
        # Get the lineup object after insertion, so we can insert the proper lineup_id
        matching_lineups = db_int.get_lineups_by_event_and_apparatus_and_school(
            lineup.event_id,
            lineup.apparatus_name,
            lineup.school_id
        )
        assert len(matching_lineups) == 1, f"Expected 1 lineup, got {len(matching_lineups)}."
        matching_lineup: Lineup = matching_lineups[0]
        lineup_entry.lineup_id = matching_lineup.lineup_id

        # Checking to see if the LineupEntry already exists
        duplicate_found = False
        matching_lineup_entries: list[LineupEntry] = db_int.get_lineup_entries_from_lineup(matching_lineup)
        for matched_lineup_entry in matching_lineup_entries:
            if matched_lineup_entry.gymnast_id == lineup_entry.gymnast_id:
                print(f"LineupEntry for Gymnast Id {lineup_entry.gymnast_id} and Lineup Id {lineup_entry.lineup_id} already exists!")
                duplicate_found = True
                break
        if not duplicate_found:
            lineup_entries_to_insert.append(lineup_entry)

    db_int.insert(*lineup_entries)


def load_teams_from_directory(db_int: DBInterface, path_to_directory: str) -> ([School], [Gymnast]):
    team_info = []
    gymnast_info = []
    for team in os.listdir(path_to_directory):
        file = open(f"{path_to_directory}/{team}", "r")
        team_data = json.load(file)

        team_info.append(team_data["school_name"])

        for gymnast in team_data["gymnasts"]:
            gymnast["school_id"] = team_info[-1]
            gymnast_info.append(gymnast)

        file.close()

    schools = insert_missing_schools(db_int, team_info)
    gymnasts = insert_missing_gymnasts(db_int, gymnast_info)

    assert len(schools) == len(team_info), f"Found {len(schools)} schools in the DB matching the names. Expected {len(team_info)}."
    assert len(gymnasts) == len(gymnast_info), f"Found {len(gymnasts)} gymnasts in the DB matching the names. Expected {len(gymnast_info)}."

    return schools, gymnasts


def load_lineups_from_file(db_int: DBInterface, path_to_file: str):
    lineup_data = json.load(open(path_to_file, "r"))

    insert_missing_lineups(db_int, lineup_data)


def load_judges_from_file(db_int: DBInterface, path_to_file: str):
    judges_data = json.load(open(path_to_file, "r"))

    insert_missing_judges(db_int, judges_data)


def load_json_from_file(path_to_file: str):
    with open(path_to_file, "r") as file:
        return json.load(file)


def load_image_from_file(path: str) -> bytes | None:
    if not path:
        return None
    try:
        with open(f"../resources/images/{path}", "rb") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Could not find path \"{path}\".")
        return None
