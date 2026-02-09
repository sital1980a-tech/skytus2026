filename = input("Enter the filename: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    content = content.replace(old_word, new_word)

    with open(filename, "w") as file:
        file.write(content)

    print(f"All occurrences of '{old_word}' have been replaced with '{new_word}' in {filename}.")

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
