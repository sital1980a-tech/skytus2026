def simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    Formula: SI = (P * R * T) / 100
    """
    return (principal * rate * time) / 100

P = float(input("Enter principal amount: "))
R = float(input("Enter annual interest rate (in %): "))
T = float(input("Enter time in years: "))

SI = simple_interest(P, R, T)
print(f"Simple Interest = {SI}")
