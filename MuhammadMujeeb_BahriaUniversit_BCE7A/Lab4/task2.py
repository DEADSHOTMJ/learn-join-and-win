import json

original_dict = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roysden'},
        {'firstName': 'Mervin', 'lastName': 'Friedland'},
        {'firstName': 'Aron', 'lastName': 'Wilkins'}
    ],
    'teachers': [
        {'firstName': 'Amberly', 'lastName': 'Calico'},
        {'firstName': 'Regine', 'lastName': 'Agtarap'}
    ]
}

# Writing to JSON file
with open('data.json', 'w') as json_file:
    json.dump(original_dict, json_file)

# Reading from JSON file
with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)

print("Json file to dictionary:", json_data)
