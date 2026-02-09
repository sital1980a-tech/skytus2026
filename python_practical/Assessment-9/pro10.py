import os

directory = input("Enter directory path (leave blank for current directory): ").strip()

if not directory:
    directory = "."

all_items = os.listdir(directory)

files = [f for f in all_items if os.path.isfile(os.path.join(directory, f))]

print(f"\nFiles in '{directory}':")
for f in files:
    print(f)
