import math
# squar in math
# a =  int(input("enter number:"))
# for i in range(a):
#     print(i**2)

# even numbers
# a =  int(input("enter number:"))
# for i in range(a):
#     if i % 2 == 0:
#         print(i)

# divisible by 3 and 4,
# a =  int(input("enter number:"))
# for i in range(a):
#     if i % 3 == 0 and i % 4 == 0:
#         print(i)

# squares
# def squares(a,b):
#     for i in range(a,b+1):
#         yield i**2

# a =  int(input("enter number:"))
# b =  int(input("enter number:"))
# for i in squares(a,b):
#     print(i)

def countdown(a):
    for i in range(a, -1, -1):
        yield i

a = int(input("Enter a number: "))
for j in countdown(a):
    print(j)
