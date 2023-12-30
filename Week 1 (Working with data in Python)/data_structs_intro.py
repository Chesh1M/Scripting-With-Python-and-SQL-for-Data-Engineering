import os

### Using LISTS to save and retrieving data in python
# Initializing list containing directories of specified directory
directories = os.listdir("/workspaces/Scripting-With-Python-and-SQL-for-Data-Engineering/Week 1 (Working with data in Python)")
print(directories)
print(directories.index("useful_commands.py"))


### Using DICTIONARIES to save and retrieving data in python
# Initialize dictionary
contacts = {"firstname": "John", "lastname": "Felix"}
# Printing specific dictionary data by selected key - get method
print("Printing specific dictionary data by selected key - get method")
print(contacts.get("lastname", "Fallback output"))
# Printing all keys
print("Printing all keys")
print(contacts.keys())
# Looping through all keys
print("Looping through all keys")
for keys in contacts.keys():
    print(keys)
# Printing all values
print("Printing all values")
print(contacts.values())
# Looping through all values
print("Looping through all values")
for values in contacts.values():
    print(values)
# Looping through both key-value pair together
print("Looping through both key-value pair together")
for keys, value in contacts.items():
    print(keys + " is " + value)