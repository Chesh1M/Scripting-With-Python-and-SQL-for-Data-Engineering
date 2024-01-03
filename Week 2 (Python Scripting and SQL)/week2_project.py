'''
Week 2 project:
Command line script to find the 10 largest files in the file system 
based on the specified file extension (png, mp4, ipynb, py etc..)
Uses in memory sqlite3 database and argparse
'''

import os, argparse, sqlite3

## Create nested list to store paths and files
files_and_size = []
for root, dirs, files in os.walk('../../'):
    for file in files:
        tmp = []
        # Get and append path to tmp
        path = os.path.join(root, file)
        tmp.append(path)
        # Get and append size to tmp
        size = os.path.getsize(path)
        tmp.append(size)
        # Append tmp as a list to files_and_size list 
        files_and_size.append(tmp)


## Connect and iniialize sqlite3 and table
connection = sqlite3.connect(':memory:')
table = 'CREATE TABLE files (id integer primary key, file_names TEXT, size INTEGER)'
cursor = connection.cursor()
cursor.execute(table)
connection.commit()


## Add files_and_size into the table created
insert_query = 'INSERT INTO files (file_names, size) VALUES(?, ?)'
for item in files_and_size:
    cursor.execute(insert_query, item)
connection.commit()


## Query database to look for files matching the extension given
def find_files_and_size(extension):
    ext = '%' + extension
    variable = []
    variable.append(ext)
    
    query = '''
    SELECT file_names, size
    FROM files
    WHERE file_names like ?
    ORDER BY size desc
    LIMIT 10
    '''

    for result in cursor.execute(query, variable):
        print(result)


## Defining argparser
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_extension", help="File extension (e.g. png/jpg etc)")
    args = parser.parse_args()
    return find_files_and_size(args.file_extension)

'''
if __name__ == '__main__':
is useful because it ensures that this file can only be ran as a script
and not used as an imported module
'''
if __name__ == '__main__':
    main()