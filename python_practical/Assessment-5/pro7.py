my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter the index of the element you want to access: "))
    print(f"Element at index {index} is {my_list[index]}")

except IndexError:
    print(f"Error: Index {index} is out of range! List has {len(my_list)} elements (0 to {len(my_list)-1}).")

except ValueError:
    print("Error: Please enter a valid integer for the index.")
