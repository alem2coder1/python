import math
import random
# 1
# ounces = 28.3495231
# s = float(input("Enter the weight in grams: "))
# print(f"You have {s} grams, which is equal to {s/ounces} ounces.")

# 2
# fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
# celsius = (5 / 9) * (fahrenheit - 32)
# print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")

# 3
# for a in range(35):
#     b = 35 - a
#     if 2*a + 4*b == 94:
#         print(a,b)

# 4
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# a = list(map(int, input("Enter the list numbers separated by space: ").split()))

# for number in a:
#     if is_prime(number):
#         print(number, end=' ')
# 5
# my_list = input("Enter the list numbers separated by space")
# result = ' '.join(my_list)
# print(result)
# 6
# def reverse_words(sentence):
#     words = sentence.split()
#     reversed_words = words[::-1]
#     reversed_sentence = ' '.join(reversed_words)
#     return reversed_sentence
# user_input = input("Enter a sentence: ")
# result = reverse_words(user_input)
# print("Reversed Sentence:", result)

# user_input = input("Enter a sentence: ")
# words = user_input.split()
# words.reverse()
# result =' '.join(words)
# print("Reversed Sentence:", result)
# 6
# def has_adjacent_3(nums):
#     for i in range(len(nums) - 1):
#         if nums[i] == 3 and nums[i + 1] == 3:
#             return True
#     return False
# a = list(map(int, input("Enter the list numbers separated by space: ").split()))
# result = has_adjacent_3(a)

# print(result)
# 7
# def spy_game(nums):
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == 0:
#                     for k in range(j + 1, len(nums)):
#                         if nums[k] == 7:
#                             return True
#     return False

# a = list(map(int, input("Enter the list numbers separated by space: ").split()))
# result = spy_game(a)

# print(result)
# 8

# def sphere_volume(radius):
#     if radius < 0:
#         return "Radius cannot be negative"
#     else:
#         volume = (4/3) * math.pi * radius**3
#         return volume

# radius = float(input("Enter the radius of the sphere: "))
# result = sphere_volume(radius)

# print(f"The volume of the sphere with radius {radius} is {result}")
# 9
# def unique_elements(input_list):
#     unique_list = []
#     for element in input_list:
#         if element not in unique_list:
#             unique_list.append(element)
#     return unique_list

# original_list = list(map(int, input("Enter the list numbers separated by space: ").split()))
# result = unique_elements(original_list)

# print("Original List:", original_list)
# print("Unique Elements:", result)

# 10
# def is_palindrome(word):
#     # Remove spaces and convert to lowercase for case-insensitive comparison
#     cleaned_word = ''.join(word.split()).lower()

#     # Check if the cleaned word is the same backward and forward
#     return cleaned_word == cleaned_word[::-1]

# # Example usage:
# user_input = input("Enter a word or phrase: ")
# result = is_palindrome(user_input)

# if result:
#     print(f"{user_input} is a palindrome.")
# else:
#     print(f"{user_input} is not a palindrome.")
# 11
# a = list(map(int, input("Enter the list numbers separated by space: ").split()))
# for i in a:
#     s = '*' * i
#     print(s,' ', end='')

def random_num():
    return random.randint(1, 20)

def guess_num():
    secret_number = random_num()
    i = 0
    while True:
        i += 1
        guess = int(input("Enter a number between 1 and 20: "))

        if guess == secret_number:
            print(f"You got it!{i}")
            break
        elif guess < secret_number:
            print("Your guess is too low!")
        else:
            print("Your guess is too high!")

guess_num()