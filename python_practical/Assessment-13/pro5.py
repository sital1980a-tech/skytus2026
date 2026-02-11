import math

class Shape:
    def area(self):
        pass  

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def print_area(shape):
    print(f"The area is: {shape.area():.2f}")


shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 7)
]

for shape in shapes:
    print_area(shape)
