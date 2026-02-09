lower_bound = int(input("Enter the lower bound of the range: "))
upper_bound = int(input("Enter the upper bound of the range: "))

num = float(input("Enter the number to check: "))

if lower_bound <= num <= upper_bound:
    print(f"{num} lies within the range {lower_bound} and {upper_bound}.")
else:
    print(f"{num} does not lie within the range {lower_bound} and {upper_bound}.")
