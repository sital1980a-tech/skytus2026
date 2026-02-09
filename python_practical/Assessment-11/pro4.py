with open("output.txt", "w") as file:

    for i in range(5):
        sentence = input(f"Enter sentence {i+1}: ")
        file.write(sentence + "\n")  

print("All sentences have been written to output.txt")
