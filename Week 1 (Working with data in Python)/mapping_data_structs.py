import os
### Mapping data structs
## Initialize list of files/directories in home directory
home_items = os.listdir("/workspaces/Scripting-With-Python-and-SQL-for-Data-Engineering")
print("\n\nFiles & directories in home directory: ", home_items, "\n")

## Initialize empty dictionary to store these directory items
home_content = {"files": [], "directories": []}

## Initialize list of absolute paths of the files & directories in home directory by joining the path and file/directory name
home_paths = [os.path.join('/workspaces/Scripting-With-Python-and-SQL-for-Data-Engineering', item) for item in home_items]

## Append the absolute paths into the empty dictionary
for path in home_paths:
    if os.path.isdir(path):
        home_content['directories'].append(path)
    if os.path.isfile(path):
        home_content['files'].append(path)
print("Files and Directories separated with absolute paths:\n", home_content)

## Print files
print("\nFiles:")
for files in home_content.get('files'):
    print(files)

print("\nDirectories:")
for item in home_content.get('directories'):
    print(item)
