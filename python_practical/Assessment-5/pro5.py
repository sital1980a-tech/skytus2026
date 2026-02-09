filename = input("Enter the filename to open: ")

file = None  

try:
    file = open(filename, 'r')
    content = file.read()
    print("File content:\n")
    print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

except IOError:
    print(f"Error: An unexpected I/O error occurred while opening '{filename}'.")

finally:

    if file:
        file.close()
        print("File has been closed (resource cleaned up).")
    else:
        print("No file to close.")
