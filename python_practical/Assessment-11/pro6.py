filename = input("Enter the filename: ")
search_word = input("Enter the word to search for: ")

try:
    
    with open(filename, "r") as file:
    
        for line in file:
            if search_word in line:
                print(line, end="")  

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
