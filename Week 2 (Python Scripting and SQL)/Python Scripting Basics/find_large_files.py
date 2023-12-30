import os

# create dictionary to save file name as keys, file size as values
file_metadata = {}

# walk the filesys
for root, directories, files in os.walk('..'):
    for _file in files:
        full_path = os.path.join(root, _file) # get absolute paths of all files in the system
        file_size = os.path.getsize(full_path) # get file size of each file (in bytes by default)
        file_metadata[full_path] = file_size

        # format print by b, kb, mb
        if file_size <= 1000:
            print(f"Size: {file_size}b - File: {full_path}")
        elif file_size > 1000 and file_size <= 1000000:
            print(f"Size: {file_size/1024:.2f}kb - File: {full_path}")
        else:
            print(f"Size: {file_size/1024/1024:.2f}mb - File: {full_path}")

print()
# print top 5 biggest files
counter = 0
for file, size in sorted(file_metadata.items(), key=lambda x:x[1], reverse=True):
    if counter < 5:
        if size <= 1000:
            print(f"Size: {size}b - File: {file}")
        elif size > 1000 and size < 1000000:
            print(f"Size: {size/1024:.2f}kb - File: {file}")
        else:
            print(f"Size: {size/1024/1024:.2f}mb - File: {file}")
        counter += 1
    else:
        break
    