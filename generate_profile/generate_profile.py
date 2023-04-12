import json

# Load the JSON data from a file
with open("potato.json", "r") as file:
    data = json.load(file)

for i in range(300):
    data['MappingState']['ButtonMappingStates19']['PhysicalInButtonControlId'] = i

    with open(f"profile_{i}.txt", "w") as file:
        json.dump(data, file, separators=(",",":"))

