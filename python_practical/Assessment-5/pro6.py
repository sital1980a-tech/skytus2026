class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be 18 or older"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print(f"Age {age} is valid. Access granted!")

try:
    age = int(input("Enter your age: "))
    check_age(age)

except InvalidAgeError as e:
    print(f"InvalidAgeError: {e.age} is not allowed. {e.message}")

except ValueError:
    print("Error: Please enter a valid integer for age.")
