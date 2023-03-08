# class myclass:
#     x = 5
# p1 = myclass()
# print (p1.x)
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()
# class Person:
#     def _init_(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age
#         pass
        
#     def myfunc(abc):
#         print ("hello my name is " + abc.name)
#         print ("I am {abc.age} old")
#         p1.age = 40
#         del p1.age
        

# p1 = Person ("John", 36)
# p1.myfunc()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunc(abc):
        print ("hello my name is " + abc.name)
        print ("I am {self.age} old")
p1 = Person ("John", 36)
p1.myfunc()