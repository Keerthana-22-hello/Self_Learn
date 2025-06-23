# tasks for abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        print("Rectangle area..")
class Circle(Shape):
    def area(self):
        print("Circle area..")

r=Rectangle()
r.area()

c=Circle()
c.area()
