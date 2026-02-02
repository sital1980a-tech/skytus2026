num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > 0 and num2 > 0 and (num1 > 10 or num2 > 10):
    print("Both numbers are positive and at least one is greater than 10")
else:
    print("Condition not met")
