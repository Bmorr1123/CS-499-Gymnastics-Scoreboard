import os
import json_management
from db_interface import DBInterface

WIPE_DB_AFTER = False


def main():
    print(os.listdir())
    database_interface = DBInterface("../db_setup/.env")
    json_management.load_teams_from_directory(
        database_interface,
        "../resources/teams"
    )
    json_management.insert_missing_events(
        database_interface,
        [
            {
                "event_name": "Test Event",
                "event_location": "Test Location",
                "event_date": "2020-05-21"
            }
        ]
    )
    json_management.insert_missing_judges(
        database_interface,
        [
            {
                "first_name": "Jeff",
                "last_name": "Winger",
                "event_id": "Test Event",
                "apparatus_name": "Vault"
            },
            {
                "first_name": "Jeb",
                "last_name": "Wing",
                "event_id": "Test Event",
                "apparatus_name": "Vault"
            }
        ]
    )
    json_management.load_lineups_from_file(
        database_interface,
        "../resources/lineups/lineups.json"
    )

    if WIPE_DB_AFTER:
        wipe_database(database_interface)

def wipe_database(db_interface: DBInterface):
    db_interface.delete(*db_interface.get_judges())
    db_interface.delete(*db_interface.get_lineup_entries())
    db_interface.delete(*db_interface.get_lineups())
    db_interface.delete(*db_interface.get_events())
    db_interface.delete(*db_interface.get_gymnasts())
    db_interface.delete(*db_interface.get_schools())

    print("WIPED THE DATABASE")


if __name__ == "__main__":
    main()
