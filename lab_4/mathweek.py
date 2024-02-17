import math
# 把角度转换值
# def radians(deg):
#     yield deg * math.pi / 180

# deg = float(input("Enter degrees: "))
# rad = radians(deg)
# for i in rad:
#     print(i)
# trapezoid area
# class trapezoid():
#     def __init__(self, edge, side, height):
#         self.edge = edge
#         self.side = side
#         self.height = height
    
#     def area(self):
#         return ((self.edge + self.side) * self.height) / 2

# a = trapezoid(5, 6, 5)
# print(a.area()) 


# def arearegular(n, s):
#     return (n * s**2) / (4 * math.tan(math.pi / n))

# sidess = int(input("Input number of sides: "))
# lengthside = float(input("Input the length of a side: "))

# area = arearegular(sidess,lengthside)

# print(int(area))


def calculate_polygon_area(n, s):
    return n*s

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
area = calculate_polygon_area(n,s)

print(int(area))