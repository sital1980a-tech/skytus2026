file1 = input("Enter the first filename: ")
file2 = input("Enter the second filename: ")
output_file = input("Enter the third filename to save merged content: ")

try:
    with open(file1, "r") as f1:
        content1 = f1.read()

    with open(file2, "r") as f2:
        content2 = f2.read()

    with open(output_file, "w") as out:
        out.write(content1)
        out.write("\n")  
        out.write(content2)

    print(f"Contents of '{file1}' and '{file2}' have been merged into '{output_file}'.")

except FileNotFoundError as e:
    print(f"Error: {e}")
