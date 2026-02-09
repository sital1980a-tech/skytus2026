from datetime import datetime

date1_str = input("Enter the first date (YYYY-MM-DD): ")
date2_str = input("Enter the second date (YYYY-MM-DD): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")


diff = abs(date2 - date1)

print(f"The difference between the two dates is {diff.days} days.")
