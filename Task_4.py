"""
Design a BankAccount class with methods for deposit, withdrawal, and balance inquiry.
Input:
account = BankAccount()
account.deposit(1000)
account.withdraw(200)
account.get_balance()
"""

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Balance after deposit: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Balance after withdrawal: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

account = BankAccount()
account.deposit(1000)
account.withdraw(200)
print(f"Current balance: {account.get_balance()}")

"""
Output : 
Balance after deposit: 1000
Balance after withdrawal: 800
Current balance: 800

Process finished with exit code 0
"""