sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")

if word in sentence:
    print(f"The word '{word}' is present in the sentence.")
else:
    print(f"The word '{word}' is not present in the sentence.")
