correct_username = "user123"
correct_password = "password123"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password. Please try again.")
