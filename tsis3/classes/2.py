class Shape:
    def __init__ (self, lenght):
     self.lenght = lenght
    
    class Square:
      def __init__ (self, edge):
          self.edge = edge
          
    def area (self):
        return self.lenght * self.lenght
    
a = Shape (int(input()))
b = Shape.area(a)
print (b)