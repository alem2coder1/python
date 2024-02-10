import math
# def upper_txt(s):
#     if len(s) > 0:
#         return s.upper()
#     else:
#         return False

# a = input("Enter a string: ")
# result = upper_txt(a)

# if result:
#     print("Uppercase string:", result)
# else:
#     print("String is empty.")

# class Shape:
#     def __init__(self):
#         pass  

#     def area(self):
#         return 0 


# class Square(Shape):
#     def __init__(self, length):
#         super().__init__()
#         self.length = length

#     def area(self):
#         return self.length ** 2  

# square_length = float(input("Enter the length of the square: "))
# square = Square(square_length)
# print("Area of Square:", square.area())

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__()
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# rectangle_length = float(input("Enter the length of the rectangle: "))
# rectangle_width = float(input("Enter the width of the rectangle: "))

# rectangle = Rectangle(rectangle_length, rectangle_width)
# print("Area of Rectangle:", rectangle.area())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"({self.x}, {self.y})")
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

x1 = float(input("Enter x-coordinate of point1: "))
y1 = float(input("Enter y-coordinate of point1: "))
point1 = Point(x1, y1)

x2 = float(input("Enter x-coordinate of point2: "))
y2 = float(input("Enter y-coordinate of point2: "))
point2 = Point(x2, y2)

print("Coordinates of point1:")
point1.show()

print("Coordinates of point2:")
point2.show()

dx = float(input("Enter displacement in x-direction for point1: "))
dy = float(input("Enter displacement in y-direction for point1: "))
point1.move(dx, dy)

print("New coordinates of point1 after moving:")
point1.show()

distance = point1.dist(point2)
print("Distance between point1 and point2:", distance)
# 
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} accepted. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal of ${amount} accepted. Current balance: ${self.balance}")
            else:
                print("Insufficient funds. Withdrawal denied.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

# Instantiate a BankAccount object
account = BankAccount("John Doe", 1000)

# Test deposit method
account.deposit(500)
account.deposit(-200)  # Invalid deposit
print()

# Test withdraw method
account.withdraw(200)
account.withdraw(1500)  # Attempt to withdraw more than balance
account.withdraw(-100)  # Invalid withdrawal
# 
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example list of numbers
numbers = [2, 3, 5, 7, 8, 11, 13, 17, 19, 23, 29, 31, 37]

# Filter prime numbers using filter function and lambda
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list:", prime_numbers)
