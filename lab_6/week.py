import shutil
import os

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"文件 {source} 成功复制到 {destination}")
    except OSError as e:
        print(f"复制文件时出错: {e}")

source_file = "/Users/alemkaken/Desktop/folder1/row.txt"
destination_folder = "/Users/alemkaken/Desktop/folder2/"

# 确保目标文件夹存在
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

copy_file(source_file, destination_folder)
