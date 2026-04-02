# Shape Area Calculator (Polymorphism) 
#A graphics application needs to calculate the area of different shapes. Create classes Circle, Rectangle, and Triangle, each having an area() method. Demonstrate polymorphism by calling the same method for different objects. 
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Circle Area:", 3.14 * self.r * self.r)

class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        print("Rectangle Area:", self.l * self.w)

class Triangle:
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        print("Triangle Area:", 0.5 * self.b * self.h)

c = Circle(5)
r = Rectangle(10, 4)
t = Triangle(6, 8)

c.area()
r.area()
t.area()