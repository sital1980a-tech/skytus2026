file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        text = file.read()  

    text = text.lower()

    for char in ",.!?;:\n":
        text = text.replace(char, " ")

    words = text.split()

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("Word frequencies in the file:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
