import json
import uuid



# Parse the JSON data
cities_data = None
with open('korea.json', 'r') as f: 
    cities_data = json.load(f)

# Function to add UUIDs
def add_uuids(data):
    for city in data:
        # Assign a UUID to the city
        city['id'] = str(uuid.uuid4())
        for spot in city['cool_spots']:
            # Assign a UUID to each cool spot
            spot['id'] = str(uuid.uuid4())

# Add UUIDs to the cities and cool spots
add_uuids(cities_data)

# Output the modified JSON with UUIDs
output_json = json.dumps(cities_data, indent=2)
print(output_json)

# Optionally, you can save the output to a new JSON file
with open('korea-uuids.json', 'w') as f:
    f.write(output_json)
