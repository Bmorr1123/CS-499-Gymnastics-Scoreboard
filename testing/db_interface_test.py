from db_interface import DBInterface
from db.models import School, Event, Gymnast, Lineup, LineupEntry, Judge
import os


DELETE_CREATED_DATA = False


def create_school(db_int: DBInterface) -> School:
    schools = db_int.get_school_by_name("Louisiana State University")
    if len(schools) == 0:  # Creates LSU if it doesn't exist
        db_int.insert(
            School(
                school_name="Louisiana State University"
            )
        )

    schools = db_int.get_school_by_name("Louisiana State University")
    for school in schools:
        print(f"School Id: {school.school_id}, School Name: {school.school_name}")

    assert len(schools) == 1 and schools[0].school_name == "Louisiana State University", "Could not find LSU in DB"

    return schools[0]


def create_gymnasts(db_int: DBInterface, school: School) -> [Gymnast]:
    gymnasts = db_int.get_gymnasts_from_school(school)
    # to_make contains Gymnasts to make IF they don't already exist
    to_make = [
        Gymnast(
            first_name="Elena",
            last_name="Arenas",
            major="Business",
            classification="Senior",
            school_id=school.school_id
        ),
        Gymnast(
            first_name="Sierra",
            last_name="Ballard",
            major="Finance",
            classification="Graduate",
            school_id=school.school_id
        )
    ]
    i = 0
    while i < len(to_make):
        tm_gymnast = to_make[i]
        for db_gymnast in gymnasts:
            if db_gymnast.first_name == tm_gymnast.first_name and db_gymnast.last_name == tm_gymnast.last_name:
                print(f"Found {tm_gymnast.first_name} {tm_gymnast.last_name} in DB. Skipping.")
                to_make.pop(i)
                i -= 1  # We need to decrement i so that we don't skip a gymnast
                break
        i += 1
    db_int.insert(*to_make)
    gymnasts = db_int.get_gymnasts_from_school(school)
    assert len(gymnasts) >= 2, "There should be at least two gymnasts in the DB for LSU"

    return gymnasts

# print(db_int.get_gymnasts_from_school(school))

def main():
    db_int = DBInterface()

    lsu = create_school(db_int)
    print(lsu)
    gymnasts = create_gymnasts(db_int, lsu)
    for gymnast in gymnasts:
        print(gymnast)

    if DELETE_CREATED_DATA:
        db_int.delete(*gymnasts)  # We must delete the gymnasts before we delete LSU
        db_int.delete(lsu)

if __name__ == "__main__":
    main()
