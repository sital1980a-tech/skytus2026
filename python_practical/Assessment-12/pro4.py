class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def find_area(self):
        return self.length * self.width

    def find_perimeter(self):
        return 2 * (self.length + self.width)


rect1 = Rectangle(10, 5)

print("Length:", rect1.length)
print("Width:", rect1.width)
print("Area:", rect1.find_area())
print("Perimeter:", rect1.find_perimeter())
