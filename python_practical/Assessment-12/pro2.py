class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  
        self.balance = balance                

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Current balance: ${self.balance}")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Account holder: {self.account_holder}, Balance: ${self.balance}")


my_account = BankAccount("Alice", 1000)
my_account.check_balance()
my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(1500)
my_account.check_balance()
