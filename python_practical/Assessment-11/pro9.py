import csv

filename = input("Enter the CSV filename: ")

try:
    
    with open(filename, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)  

    if not data:
        print("The file is empty.")
    else:
        
        col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]

    
        for row in data:
            formatted_row = " | ".join(f"{item:<{col_widths[i]}}" for i, item in enumerate(row))
            print(formatted_row)

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
