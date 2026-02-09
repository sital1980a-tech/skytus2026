lines_to_append = [
    "This is the first new line.",
    "Here is the second new line.",
    "And this is the third one."
]

with open("output.txt", "a") as file:  
    for line in lines_to_append:
        file.write(line + "\n")  

print("Lines have been appended to output.txt")
