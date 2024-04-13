import os

# Task 1: 列出目录和文件
def list_directories_and_files(path):
    directories = []
    files = []
    
    items = os.listdir(path)
    
    for item in items:
        item_path = os.path.join(path, item)
        
        if os.path.isdir(item_path):
            directories.append(item)
        else:
            files.append(item)
            
    return directories, files

# Task 2: 检查路径访问
def check_path_access(path):
    access_info = {}
    access_info['exists'] = os.path.exists(path)
    access_info['readable'] = os.access(path, os.R_OK)
    access_info['writable'] = os.access(path, os.W_OK)
    access_info['executable'] = os.access(path, os.X_OK)
    return access_info

# Task 3: 检查路径是否存在和详细信息
def check_path(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        return True, directory, filename
    else:
        return False, None, None

# Task 4: 计算文件中的行数
def count_lines(filename):
    line_count = 0
    with open(filename, 'r') as file:
        for line in file:
            line_count += 1
    return line_count

# Task 5: 从文件中读取行并将其写入另一个文件
def write_list_to_file(filename, my_list):
    with open(filename, 'w') as file:
        for item in my_list:
            file.write(str(item))

# Task 6: 为字母表中的每个字母生成文件
def generate_files():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in letters:
        filename = f"Letters/{letter}.txt"
        with open(filename, 'w') as file:
            file.write(filename)

# Task 7: 删除字母表中每个字母的文件
def delete_files(path):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in letters:
        file_path = os.path.join(path, f"Letters/{letter}.txt")
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print(f"File '{file_path}' does not exist.")

specified_path = "/Users/alemkaken/Documents/Github/python/lab_6"

# Task 1: 列出目录和文件
directories, files = list_directories_and_files(specified_path)
print("Directories:")
for directory in directories:
    print(directory)

print("\nFiles:")
for file in files:
    print(file)

# Task 2: 检查路径
access_info = check_path_access(specified_path)
print(f"\nPath: {specified_path}")
print(f"Exists: {access_info['exists']}")
print(f"Readable: {access_info['readable']}")
print(f"Writable: {access_info['writable']}")
print(f"Executable: {access_info['executable']}")

# Task 3: 检查路径是否存在和详细信息
exists, directory, filename = check_path(specified_path)
if exists:
    print("\nPath exists.")
    print("Directory:", directory)
    print("Filename:", filename)
else:
    print("\nPath does not exist.")

# Task 4:
filename = "row.txt"
num_lines = count_lines(filename)
if num_lines > 0:
    print("\nNumber of lines:", num_lines)

# Task 5:从文件中读取行并将其写入另一个文件
filename = "row.txt"
my_list = []
with open(filename, 'r') as file:
    for line in file:
        my_list.append(line)
write_list_to_file("output.txt", my_list)

# Task 6: 为字母表中的每个字母生成文件
generate_files()

delete_files(specified_path)
