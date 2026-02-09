balance = 5000 

withdrawal_amount = float(input("Enter the amount to withdraw: "))

if withdrawal_amount <= balance:
    balance -= withdrawal_amount  
    print(f"Transaction successful! You have withdrawn {withdrawal_amount}.")
    print(f"Your remaining balance is {balance}.")
else:
    print("Insufficient balance! Please try a smaller amount.")
