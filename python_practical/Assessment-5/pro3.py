filename = input("Enter the filename to open: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n")
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
