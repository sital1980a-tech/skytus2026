try:
    # Take two inputs and divide them
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    
    result = numerator / denominator
    print("Result:", result)

    # Accessing a list element
    sample_list = [1, 2, 3]
    index = int(input("Enter an index to access the list: "))
    print("Element at index", index, "is", sample_list[index])

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter integers only.")

except IndexError:
    print("Error: List index out of range!")

except Exception as e:  # Catch-all for any other exception
    print("An unexpected error occurred:", e)
