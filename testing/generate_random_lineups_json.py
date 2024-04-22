import json, random
from pprint import pprint


exit(0)
APPEND_MODE = False
SCHOOL_FILE_PATH = "georgia"

with open(f"../resources/teams/{SCHOOL_FILE_PATH}.json", "r") as file:
    data = json.load(file)

if APPEND_MODE:
    with open(f"../resources/lineups/{SCHOOL_FILE_PATH}_lineup.json", "r") as file:
        lineup_data = json.load(file)
else:
    lineup_data = []

for event in ("Vault", "Floor", "Beam", "Bars"):
    gymnast_list = []
    while len(gymnast_list) < 6:
        gymnast = data["gymnasts"][random.randint(0, len(data["gymnasts"]) - 1)]
        if gymnast not in gymnast_list:
            gymnast_list.append(gymnast)

    gymnast_list = [f"{gymnast["first_name"]}|{gymnast["last_name"]}" for gymnast in gymnast_list]

    lineup_data.append(
        {
            "school_id": data["school_name"],
            "event_id": "Test Event",
            "apparatus_name": event,
            "gymnasts": gymnast_list
        }
    )

json.dump(lineup_data, open(f"../resources/lineups/{SCHOOL_FILE_PATH}_lineup.json", "w+"), indent=4)