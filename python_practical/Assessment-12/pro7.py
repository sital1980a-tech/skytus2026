import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def find_area(self):
        return math.pi * self.radius ** 2

    def find_circumference(self):
        return 2 * math.pi * self.radius


circle1 = Circle(7)

print("Radius:", circle1.radius)
print("Area:", circle1.find_area())
print("Circumference:", circle1.find_circumference())
