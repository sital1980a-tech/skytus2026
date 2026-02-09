def calculate_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    elif units <= 300:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    else:
        bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 12
    return bill

units_consumed = float(input("Enter the number of units consumed: "))

bill = calculate_bill(units_consumed)

print(f"Total electricity bill for {units_consumed} units is: ₹{bill:.2f}")
