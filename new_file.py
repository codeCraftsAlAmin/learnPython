from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, dm1, dm2):
        self.dm1 = dm1
        self.dm2 = dm2
    
    @abstractmethod
    def area(self):
        pass
    

class Triangle(Shape):
    def area(self):
        return 0.5 * (self.dm1) * (self.dm2)
    
    
class Rectangle(Shape):
    def area(self):
        return (self.dm1) * (self.dm2)
    

t = Triangle(10, 20)
print(t.area())

r = Rectangle(10, 20)
print(r.area())