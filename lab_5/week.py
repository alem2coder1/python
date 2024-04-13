import re

def check_pattern(string):
    pattern = r"^[A-Z].{6}[a-z]$"
    if re.match(pattern, string):
        return True
    else:
        return False

test_string = input("请输入一个字符串：")
if check_pattern(test_string):
    print("符合要求")
else:
    print("不符合要求")