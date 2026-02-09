numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter an index number: "))
    print("Value at index", index, "is:", numbers[index])

except IndexError:
    print("Error: Index out of range! Please enter a valid index.")

except ValueError:
    print("Error: Please enter an integer value.")

else:
    print("Accessed successfully 👍")

finally:
    print("Program execution completed.")

