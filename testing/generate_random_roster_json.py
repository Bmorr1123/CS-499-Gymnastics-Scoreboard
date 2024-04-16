import json, random
from pprint import pprint

with open("../resources/teams/uky.json", "r") as file:
    data = json.load(file)

lineup_data = []

for event in ("Vault", "Floor", "Beam", "Bars"):
    gymnast_list = []
    while len(gymnast_list) < 6:
        gymnast = data["gymnasts"][random.randint(0, len(data["gymnasts"]) - 1)]
        if gymnast not in gymnast_list:
            gymnast_list.append(gymnast)

    gymnast_list = [f"{gymnast["first_name"]} {gymnast["last_name"]}" for gymnast in gymnast_list]

    lineup_data.append(
        {
            "school_id": "University of Kentucky",
            "event_id": "Test Event",
            "apparatus_name": event,
            "gymnasts": gymnast_list
        }
    )

json.dump(lineup_data, open("../resources/lineups/lineups.json", "w+"), indent=4)