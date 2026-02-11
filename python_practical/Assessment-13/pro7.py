class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    # Setter methods
    def set_account_holder(self, name):
        self.__account_holder = name

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.__balance}")

    def display_details(self):
        print("\nAccount Details:")
        print("Account Number:", self.__account_number)
        print("Account Holder:", self.__account_holder)
        print("Balance:", self.__balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_number, account_holder, balance)
        self.__interest_rate = interest_rate

    def get_interest_rate(self):
        return self.__interest_rate

    def set_interest_rate(self, rate):
        if rate > 0:
            self.__interest_rate = rate

    def add_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)
        print(f"Interest added: {interest}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=1000):
        super().__init__(account_number, account_holder, balance)
        self.__overdraft_limit = overdraft_limit

    
    def get_overdraft_limit(self):
        return self.__overdraft_limit

    def set_overdraft_limit(self, limit):
        if limit >= 0:
            self.__overdraft_limit = limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.get_balance() + self.__overdraft_limit:
            print("Overdraft limit exceeded.")
        else:
            
            new_balance = self.get_balance() - amount
        
            self._BankAccount__balance = new_balance
            print(f"Withdrawn {amount}. New balance: {new_balance}")


# -------- Testing --------

savings = SavingsAccount("SA1001", "Alice", 5000)
savings.deposit(1000)
savings.add_interest()
savings.display_details()

current = CurrentAccount("CA2001", "Bob", 3000, 2000)
current.withdraw(4500)   
current.display_details()
