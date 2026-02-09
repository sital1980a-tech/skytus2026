file_name = input("Enter the file name: ")

try:

    with open(file_name, 'r') as file:
    
        lines = file.readlines()
        
        line_count = len(lines)
    print(f"The file has {line_count} lines.")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
