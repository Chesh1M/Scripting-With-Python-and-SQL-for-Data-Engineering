import os

print()
## Dictionary commands
# Initializing dictionary of home directory paths
home_items = os.listdir("/workspaces/Scripting-With-Python-and-SQL-for-Data-Engineering")
home_content = {"files": [], "directories": []}
for item in home_items:
    if os.path.isfile(item):
        home_content['files'].append(item)
    if os.path.isdir(item):
        home_content['directories'].append(item)
print("Home content dictionary:", home_content)
# Printing specific dictionary values by selected key - get method
print(home_content.get("directories", "Fallback output"))
# Looping through each value for the specified key
for values in home_content.get("directories"):
    print(values)
# Printing values and keys 
print(home_content.values())
print(home_content.keys())

print()
## Find out what methods are available in an object
for methods in dir(tuple()):
    if methods.startswith('__'):
        continue
    print(methods)


print()
## List comprehension
# Single layer
items = ['a', '1', '23', 'b', '4', 'c', 'd']
numbers = [item for item in items if item.isnumeric()]
print(numbers)

# Nested
items_2d = [['a', '1', '23', 'b', '4', 'c', 'd'], ['a', '1', '23', 'b', '4', 'c', 'd']]
numbers_2 = [item for parent in items_2d for item in parent if item.isnumeric()]
print(numbers_2)
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
short_planets = [planet for sub_list in planets for planet in sub_list if len(planet) < 6]
print(short_planets)

    