def check_triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Sides must be positive numbers."
    
    if a == b == c:
        return "Equilateral Triangle"
    elif a == b or b == c or a == c:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

triangle_type = check_triangle_type(side1, side2, side3)

print("The triangle is:", triangle_type)
