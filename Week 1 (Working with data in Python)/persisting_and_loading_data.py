'''
### Reading csv/sql files
### e.g. file w data "populate.sql"

## Method 1 (using open and close)
sql_file = open("populate.sql")
sql_contents = sql_file.readlines() # or read() but that will just read as one big chunk
print(sql_contents)
sql_file.close()

## Method 2 (using with)
with open("population.sql") as sql_file:
    sql_contents = sql_file.readlines()

## Method 3 (using pandas)
import pandas as pd
df = pd.read_csv("wine-ratings-small.csv")
print(df.head())

'''
### Working with JSON
import json
## Conerting Python to JSON
data = {"name": "Alfredo", "data": [], "valid": True}
print(json.dumps(data)) # dump string

## Conerting JSON to Python (dictionary)
json_output = '{"name": "Alfredo", "data": 1, "valid": true}'
loaded_json = json.loads(json_output) # <- this is a dictionary
print(loaded_json)
print(loaded_json['valid'])

'''
## Example given a json file 'wine-ratings.json'
with open('wine-ratings.json') as f:
    loaded_json = json.load(f)
print(loaded_json) # <- dictionary from the json file 
'''



### Saving data from python to disk
data = {"firstname": "Aowen", "lastname": "Chin", "valid": True} # valid True helps you see that it is indeed converting to json if True becomes lowercase
with open("sample_data.json", "w") as f:
    json.dump(data, f)