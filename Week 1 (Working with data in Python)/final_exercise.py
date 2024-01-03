import json
import os
dir_path = '/workspaces/Scripting-With-Python-and-SQL-for-Data-Engineering/Week 1 (Working with data in Python)/'
'''
### (1) Serialize JSON from Python
# From Python, convert a dictionary into a JSON string
data = {"grape": "Cabernet Franc", "species": "Vitis vinifera", "origin": "Bordeaux, France"}
json_data = json.dumps(data)
print(json_data)

# Convert a JSON string into a Python data structure
# using the previously created json string
loaded_data = json.loads(json_data)
print(loaded_data)

# Python dictionaries are not the only data structure allowed. Use lists as well
collection = [data, data]
print(collection)
# may look similar in the output, but the difference is that JSON is now a string
print(json.dumps(collection))

# now use the `.dump()` JSON method (note no 's'!) to save it to a new JSON file
with open(dir_path+'sample.json', 'w') as f:
    json.dump(collection, f)

 
### (2) JSON Formatting
## It is common for HTTP APIs and JSON files to present JSON as a single line. In this section, you will use formatting options in the JSON module to improve the readability of nested information in JSON
# define a nested data structure in a single line
grape_data = {"name": "Cabernet France", "regions": [{"country": "France", "sub-regions": ["Bordeaux", "Loire Valley"]},{"country": "Italy", "sub-regions": ["Apulia", "Tuscany"]}, {"country": "Argentina", "sub-regions": ["Mendoza", "Lujan de Cuyo", "Salta"]}]} 
# Serialize the Python dictionary to a JSON string, but using extra formatting options, like sorted keys
# and using 4 spaces for indentation
data_as_json = json.dumps(grape_data, sort_keys=True, indent=4)
print(data_as_json)

# Try other variations like indenting 2 spaces and not sorting keys:
data_as_json = json.dumps(grape_data, sort_keys=False, indent=2)
print(data_as_json)

'''


### (3) Serialize JSON from a file
## The process of reading a foreign format like JSON and loading it into Python is called serializing it.
# When working with paths, always ensure these paths are reachable and correct
print(os.path.exists(dir_path+'wine-ratings.json'))

# read the JSON file and then parse it using the `.load()` method
# note the subtle difference, this is the `.load()` method (no 's'), not `.loads()`
with open(dir_path+'wine-ratings.json') as f:
    loaded_json = json.load(f)
print(loaded_json.keys())
print(f"Number of items: {len(loaded_json['name'])}")



### (4) Serialize from Python to a JSON file - connected to (3)
## Now that you've loaded JSON from a file into Python, do some data sampling, extract some interesting fields and then save the newly manipulated data to a file on disk as JSON.
names = loaded_json['name']
print(names)

# these names are using a dictionary with an index, like {"0": "Some Name and Year"}. 
# Convert the data to use a list of only the names, like ["Some Name and Year"].
names_only = list(names.values())
print(names_only)

# now use the `.dump()` JSON method (note no 's'!) to save it to a new JSON file
with open(dir_path+'final_exercise_wine_names.json', 'w') as f:
    json.dump(names_only, f)
