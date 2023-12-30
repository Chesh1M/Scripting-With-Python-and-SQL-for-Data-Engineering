import os

def main():
    for root, directories, files in os.walk('..'): # list all roots/directories/files from the current directory
        print(f"\nRoot: {root}")
        print(f"Directories: {directories}")
        print(f"Files: {files}\n")

def list_abs_paths():
    for root, directories, files in os.walk('../../'):
        for _file in files:
            abs_path = os.path.join(root, _file)
            print(f"File path: {abs_path}")

main()
list_abs_paths()