source_file = input("Enter the filename to back up: ")
backup_file = input("Enter the backup filename: ")

try:

    with open(source_file, "r") as src:
        content = src.read() 


    with open(backup_file, "w") as backup:
        backup.write(content)  

    print(f"Backup created successfully: '{backup_file}'")

except FileNotFoundError:
    print(f"The file '{source_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
