import math
# Task 1
# 1. Define a class which has at least two methods: getString: to get a string from console input printString: to
# print the string in upper case.
class String:
    def getString(self):
        a = input()
        self.str = a
    def printString(self):
        b = self.str
        c = b.upper()
        print(c)
# Task 2:
# 2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length
# as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by
# default.
class Shape:
    def __init__(self, length):
        self.length = length
    def area(self):
        return 0
class Square(Shape):
    def area(self):
        return self.length ** 2
c = Square(4)
print(c.area())


# 3. Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by
# a length and width. The Rectangle class has a method which can compute the area.
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width
        
    def area(self):
        return self.length * self.width
a = Rectangle(1, 3)
print (a.area())

# 4. Write the definition of a Point class. Objects from this class should have a
#
#         a method show to display the coordinates of the point
#         a method move to change these coordinates
#         a method dist that computes the distance between 2 points




# 5. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals
# may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to
# make sure the account can't be overdrawn.
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        new_balance = self.balance + money
        self.balance = new_balance

    def withdraw(self, money):
        new_balance = self.balance - (money)
        if new_balance < 0:
            print(f"You can't withdraw {money:.2f}, because your balance is only {self.balance:.2f}!")
            return

        self.balance = new_balance


my_account = Account("Owner", 0)
my_account.deposit(500.7)
my_account.withdraw(500.6)
my_account.withdraw(1234)

my_account.deposit(100)
my_account.withdraw(200)

# 6. Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define
# anonymous functions.
numbers: list = [1, 55, 42, 67, 68, 69, 50]
numbers.remove(1)
   
if_prime = lambda x: all(x % i != 0 for i in range(2, x))
result_it = filter(if_prime, numbers)
result_list = list(result_it)
print(f"list of prime numbers: {result_list}")