import csv, json, pprint

with open("../resources/vault_start_values.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pprint.pp(row)