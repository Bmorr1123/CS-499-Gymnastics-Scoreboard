import os
import json_management
from db_interface import DBInterface


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
            }
        ]
    )
    json_management.load_lineups_from_file(
        database_interface,
        "../resources/lineups/lineups.json"
    )


if __name__ == "__main__":
    main()
