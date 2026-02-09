# main.py

import string_ops

text = input("Enter a string: ")

print("Uppercase:", string_ops.to_upper(text))
print("Lowercase:", string_ops.to_lower(text))
print("Reversed:", string_ops.reverse_string(text))
print("Characters:", string_ops.count_characters(text))
print("Words:", string_ops.count_words(text))
print("Palindrome:", string_ops.is_palindrome(text))
