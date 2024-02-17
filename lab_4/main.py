import datetime
# fruits = [
#     {'name': 'alem',
#     'id':'22B03',
#     'age': 18
#     },
#     {
#         'name': 'world',
#         'id': '322nm4j',
#         'age':21
#     }
# ]
# for i in fruits:
#     print(i['name'])


# a =("apple", "orange", "banana")
# i = iter(a)
# print(next(i))


# a = (i**2 for i in range(1,7))
# for i in a:
#     print(i)
# 输出时间
# x = datetime.datetime.now()
# print(x.strftime("%Y-%m-%d"))

# __init__()
# class test_:
#     def __init__(self,score,Ranking):
#         self.score = score
#         self.Ranking = Ranking

# a = test_(98,2)
# print(a.score) 

# __str__() 
class Test_:
    def __init__(self,name,Ranking):
        self.name = name
        self.Ranking = Ranking
    def __str__(self):
        return f"{self.name}({self.Ranking})"
    
a = Test_("zhangsan",2)
print(a)