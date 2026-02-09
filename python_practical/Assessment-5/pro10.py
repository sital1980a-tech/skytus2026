import re

class InvalidEmailError(Exception):
    pass

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern, email):
        raise InvalidEmailError("Invalid email format")

try:
    email = input("Enter your email address: ")
    validate_email(email)
    print("Email is valid ✅")

except InvalidEmailError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected error:", e)
