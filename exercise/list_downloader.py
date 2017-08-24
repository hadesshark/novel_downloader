import json

with open("setting.json", encoding="utf-8") as json_file:
    json_data = json.load(json_file)

print(json.dumps(json_data, skipkeys=False, indent=4))
