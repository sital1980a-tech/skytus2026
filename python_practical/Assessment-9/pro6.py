from shapes import circle_area, circle_perimeter, rect_area, rect_perimeter

r = float(input("Enter radius of circle: "))
print("Circle Area:", circle_area(r))
print("Circle Perimeter:", circle_perimeter(r))

l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
print("Rectangle Area:", rect_area(l, w))
print("Rectangle Perimeter:", rect_perimeter(l, w))
