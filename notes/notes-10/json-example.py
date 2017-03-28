import json

def write_json(data):
    with open('/tmp/output.json', 'w') as f:
        json.dump(data, f)

def read_json():
    with open('/tmp/output.json', 'r') as f:
        data = json.load(f)

    return data

my_data = {
    'name': 'Mike',
    'number': 10,
    'info': {
        'likes': None,
        'hates': None
    }
}
write_json(my_data)
new_data = read_json()
print(new_data)
