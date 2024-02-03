# True or False
a = 100
b = 3

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#    bool()
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
# The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
# "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#   Operators
#   +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y	
#   x=5
#   y=4
#   z=3
# if x > y and x > z:
#   print("x is greater than y and x is greater than z")
# else:
#   print("x is not greater than y and x is not greater than z")

#   Bitwise Operators
#   & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# << x << 2	
# >>		x >> 2
  print(100 + 5 * 3 -3 / 2**2)
#   Python Lists,数组
  list = ["alem", "world", "世界"]
  for i in list:
    print(i)

list1 = ["abc", 34, True, 40, "male"]
print(list1)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry")) 
print(thislist)
# 长度
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#   用循环输出
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
# 找出出现次数
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

myset = {"apple", "banana", "cherry"}
print(type(myset))
# 使用 set() 构造函数创建一个集合：
thisset = set(("apple", "banana", "cherry")) 
print(thisset)

s = {"app", "web", "end"}
print("banana" in s)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# 两个集合合并、
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# 删除
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# 注意：如果要删除的项目不存在，discard() 将不会引发错误。

# 您还可以使用 pop() 方法删除项目，但此方法将删除随机项目，因此您无法确定删除了哪些项目。

# pop() 方法的返回值是删除的项目。
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# 清空
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# 您可以使用 union() 方法返回一个包含两个集合中所有项目的新集合，或者使用 update() 方法将一个集合中的所有项目插入到另一个集合中：
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# 找出包含
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
# 添加不同元素
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)
# Python Dictionaries
per = {
  "name":"alem",
  "age":20,
  "sex":"male",
  "city":"world",
  "colors": ["red", "white", "blue"]
}
print(per)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x)
car["color"] = "white"
print(x) 

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x)
car["year"] = 2020
print(x)
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) 
car["year"] = 2020
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# 删除
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

# copy
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

# while
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)