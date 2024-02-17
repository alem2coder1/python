class TriangleChecker:
    def __init__(self):
        self.a = None
        self.b = None
        self.s = None
    
    def set_sides(self, a, b, s):
        self.a = a
        self.b = b
        self.s = s
    
    def is_triangle(self):
        if self.a is None or self.b is None or self.s is None:
            return "Sides are not set. Please use set_sides() method to set the sides."
        elif self.a < 0 or self.b < 0 or self.s < 0:
            return "Negative numbers won't work!"
        elif isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)) and isinstance(self.s, (int, float)):
            if self.a + self.b > self.s and self.a + self.s > self.b and self.b + self.s > self.a:
                return "Hooray, you can build a triangle!"
            else:
                return "It's a pity, but you can't make a triangle out of it."
        else:
            return "You only need to enter numbers."

checker = TriangleChecker()

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
s = int(input("Enter the third number: "))

checker.set_sides(a, b, s)
print(checker.is_triangle())
