from abc import ABC


# Abstract class
class Shape(ABC):
    # abstract methos
    def calculate_area(self):
        pass


class Rectangle(Shape):
    length = 5
    breadth = 4

    def calculate_area(self):
        return self.length * self.breadth


class Circle(Shape):
    radius = 4

    def calculate_are(self):
        return 3.14 * self.radius * self.radius


# creating an object for the class Rectangle
rec = Rectangle()

# calling the method calculate_area of Rectangle using "rec" object
print("Area of the rectangle", rec.calculate_area())

# creating an object for the class Circle
cir = Circle()

# calling the method calculate_area of Circle using "cir" object
print("Area of a circle:", cir.calculate_are())
