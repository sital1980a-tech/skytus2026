def reverse_string(s):
    """Return the reversed string"""
    return s[::-1]

text = input("Enter a string: ")
reversed_text = reverse_string(text)
print("Reversed string:", reversed_text)
