import os
import re

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "row.txt"
file_path = os.path.join(desktop_path, file_name)

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
# 1
# find_a = r'\b\w*а\w*б\w*\b'
# 2
# find_ab = r'\b\w*а\w*б{2,3}\w*\b'
# 3
# find_min = r'\b[а-я]+\b'
# 4
# find_max = r'\b[А-Я][а-я]+\b'
# 5
# find_mid = r'^а.*б$'
# Includes = re.findall(find_min, content)
# for Include in Includes:
#     print(Include)
# 6
# def replace_colon(text):
#     modified_tx = text.replace(' ', ':').replace(',', ':').replace('.', ':')
#     return modified_tx
# modified_kong = replace_colon(content)
# print(modified_kong)
# 7
# def snake_to_camel(snake_str):
#     parts = snake_str.split('_')
#     camel_case = parts[0] + ''.join(word.capitalize() for word in parts[1:])
#     return camel_case
# shexing = snake_to_camel(content)
# print(shexing)
# 8
# def split_at_uppercase(text):
#     parts = re.findall('[A-Z][^A-Z]*', text)
#     return parts

# split_parts = split_at_uppercase(content)
# print("Split parts:", split_parts)
# 9
# def insert_spaces(text):
#     modified_text = re.sub(r'(?<=[a-z])([A-Z])', r' \1', text)
#     return modified_text

# text_max = insert_spaces(content)
# print(text_max)
# 10
def camel_to_snake(camel_case):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()
    return snake_case

snake_text = camel_to_snake(content)
print(snake_text)