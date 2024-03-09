import threading
import time
import math
from functools import reduce
# 1
def multiply(numbers):
    product = reduce(lambda x, y: x * y, numbers)
    # product = reduce(lambda x, y:x+y, numbers)
    return product

numbers = [1, 2, 3, 4, 5]
result = multiply(numbers)
print(result)
# 2
z, c = 0, 0

def accepts(s):
    global z, c 
    for char in s:
        if char.isupper():
            z += 1
        elif char.islower():
            c += 1

s = input("Enter a string: ")
accepts(s)
print("Number of uppercase letters:", z)
print("Number of lowercase letters:", c)
# 3
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
# 4
def squr_root(min, sqr):
    time.sleep(min / 1000)
    return math.sqrt(sqr)

sqr = float(input("Enter a number to find its square root: "))
min_delay = int(input("Enter the delay time in milliseconds: "))

print(f"Waiting for {min_delay} milliseconds before calculating square root...")
result = squr_root(min_delay, sqr)
print(f"Square root of {sqr} after {min_delay} milliseconds is {result}")
# 5
def all_true(tuple_input):
    return all(tuple_input)

tuple_input = eval(input("Enter a tuple of boolean values (e.g., (True, False, True)): "))

print("All elements in the tuple are true:", all_true(tuple_input))
