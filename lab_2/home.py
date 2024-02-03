import math
list = [1,2,3,4,5,6,7,8,9,10]
for i in list:
   if i %i != 0:
    print(list)
    
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0:
#             return False
#     return True

# def filter_prime(numbers):
#     numlist =[]
#     for num in numbers:
#         if (is_prime(num)):
#             numlist.append(num)
#     return numlist
# input_str = input("")
# numbers = [int(num) for num in input_str.split()]
# result = filter_prime(numbers)
# for prime in result:
#  print(prime,end=' ')