import math
# this is a comment
name = input("请输入你的名字: ")
print(name)
print("hello world")
x = str(10)
y=int(10)
z=float(10.3)
print(x,y,z)
# python name The name must start with a letter or underscore
fruits = ["alem", "world", "世界"]
x, y, z = fruits
print(x, y, z)
txt = "The best things in life are free!"
for i in txt:
  print(i)
txt1 = "The best things in life are free!"
if "free" in txt1:
  print("Yes, 'free' is present.")
else: print("no, 'free' is not present")
#该upper()方法返回大写的字符串：
a = "Hello, World!"
print(a.upper())
#该lower()方法返回小写的字符串：
a = "Hello, World!"
print(a.lower())
#该strip()方法删除开头或结尾的所有空格：
a = " Hello, World! "
print(a.strip())
#该replace()方法用另一个字符串替换一个字符串：
a = "Hello, World!"
print(a.replace("World", "China"))
#该split()方法将一个字符串分割成一个列表：（list）
a = "Hello, World!"
print(a.split(","))
#字符串连接
a = "Hello"
b = "World"
c = a + b
print(c)
a = ["Hello", "World"]
result = " ".join(a)
#使用该format()方法将数字插入字符串：,您可以使用索引号{0}来确保参数放置在正确的占位符中：
age = 20
txt = "I am ten {} old"
print(txt.format(age))
age = 20
txt = f"I am ten{age} old " 
print(txt)
z = 3
x = 5
b = 7
myorder = "I am ten {2} his {0} you {1}."
print(myorder.format(z, x, b))
#转义字符允许您在通常不允许的情况下使用双引号,输出it`s，换行，回车,输出四个空格,向左移动一个位置
tx = "men bukin \"tuski as\" ishtim."
print(tx)
txt = 'It\'s camputer.'
print(txt) 
txt = "Hello\nWorld!"
print(txt) 
txt = "Hello\rWorld!"
print(txt) 
txt = "Hello\tWorld!"
print(txt)
print("Hello\bWorld")
