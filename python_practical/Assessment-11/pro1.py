filename = input("Enter the file name (with extension): ")

try:

    with open(filename, "r") as file:
        content = file.read()  
        print("\n--- File Contents ---")
        print(content)
except FileNotFoundError:
    print(f"File '{filename}' not found ❌")
except Exception as e:
    print("An error occurred:", e)
