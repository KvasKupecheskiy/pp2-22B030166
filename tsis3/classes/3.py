class Rectangle:
    def __init__ (self, lenght, widht):
        self.lenght = lenght
        self.widht = widht
    
    def area (self):
        return self.lenght * self.widht
    
a = Rectangle (int (input ()), int (input()))
print (Rectangle.area(a))