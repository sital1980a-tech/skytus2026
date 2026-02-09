class BankAccount:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")

    def show_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def account_details(self):
        print("\n--- Account Details ---")
        print("Name:", self.name)
        print("Account Number:", self.acc_no)
        print("Balance: ₹", self.balance)


def main():
    print("=== Bank Management System ===")
    name = input("Enter account holder name: ")
    acc_no = input("Enter account number: ")

    account = BankAccount(name, acc_no)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Balance Enquiry")
        print("4. Account Details")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            account.show_balance()

        elif choice == "4":
            account.account_details()

        elif choice == "5":
            print("Thank you for using the bank system.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
