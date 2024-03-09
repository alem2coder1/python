import os

# Task 1: List directories and files
def list_directories_and_files(path):
    directories = []
    files = []
    
    # Get list of items in the specified path
    items = os.listdir(path)
    
    # Separate items into directories and files
    for item in items:
        item_path = os.path.join(path, item)
        
        if os.path.isdir(item_path):
            directories.append(item)
        else:
            files.append(item)
            
    return directories, files

# Task 2: Check path access
def check_path_access(path):
    access_info = {}
    access_info['exists'] = os.path.exists(path)
    access_info['readable'] = os.access(path, os.R_OK)
    access_info['writable'] = os.access(path, os.W_OK)
    access_info['executable'] = os.access(path, os.X_OK)
    return access_info

# Task 3: Check path existence and details
def check_path(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        return True, directory, filename
    else:
        return False, None, None

# Task 4: Count lines in a file
def count_lines(filename):
    line_count = 0
    with open(filename, 'r') as file:
        for line in file:
            line_count += 1
    return line_count

# Task 5: Read lines from a file and write them to another file
def write_list_to_file(filename, my_list):
    with open(filename, 'w') as file:
        for item in my_list:
            file.write(str(item))

# Task 6: Generate files for each letter in the alphabet
def generate_files():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in letters:
        filename = f"Letters/{letter}.txt"
        with open(filename, 'w') as file:
            file.write(filename)

# Task 7: Delete files for each letter in the alphabet
def delete_files(path):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in letters:
        file_path = os.path.join(path, f"Letters/{letter}.txt")
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print(f"File '{file_path}' does not exist.")

# Example usage:
specified_path = "/Users/alemkaken/Documents/Github/python/lab_6"

# Task 1: List directories and files
directories, files = list_directories_and_files(specified_path)
print("Directories:")
for directory in directories:
    print(directory)

print("\nFiles:")
for file in files:
    print(file)

# Task 2: Check path access
access_info = check_path_access(specified_path)
print(f"\nPath: {specified_path}")
print(f"Exists: {access_info['exists']}")
print(f"Readable: {access_info['readable']}")
print(f"Writable: {access_info['writable']}")
print(f"Executable: {access_info['executable']}")

# Task 3: Check path existence and details
exists, directory, filename = check_path(specified_path)
if exists:
    print("\nPath exists.")
    print("Directory:", directory)
    print("Filename:", filename)
else:
    print("\nPath does not exist.")

# Task 4: Count lines in a file
filename = "row.txt"
num_lines = count_lines(filename)
if num_lines > 0:
    print("\nNumber of lines:", num_lines)

# Task 5: Read lines from a file and write them to another file
filename = "row.txt"
my_list = []
with open(filename, 'r') as file:
    for line in file:
        my_list.append(line)
write_list_to_file("output.txt", my_list)

# Task 6: Generate files for each letter in the alphabet
generate_files()

# Task 7: Delete files for each letter in the alphabet
delete_files(specified_path)
