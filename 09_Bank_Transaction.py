'''
Problem:
Track users bank transactions and balance .'''

'''
 Create a BankAccount class to manage balance and transactions.
 Use methods for deposit, withdraw, and display balance.

'''

class BankAccount:
    def __init__(self):
        initial = float(input("Enter initial balance: "))
        self.balance = initial
        print(f"Account created with ₹{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Credited ₹{amount}")
        print(f"Total Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Debited ₹{amount}")
        else:
            print("Insufficient balance!")
        print(f"Total Balance: ₹{self.balance}")

    def display(self):
        print(f"Available Balance: ₹{self.balance}")



acc = BankAccount()

while True:
    transaction_type = input("\n Type 'credit' to deposit, 'debit' to withdraw, or 'exit' to quit: ").lower()

    if transaction_type == 'exit':
        print("\nExiting. Final ", end='')
        acc.display()
        break

    elif transaction_type == 'credit':
        amt = float(input("Enter amount to deposit: "))
        acc.deposit(amt)

    elif transaction_type == 'debit':
        amt = float(input("Enter amount to withdraw: "))
        acc.withdraw(amt)

    else:
        print("Invalid input. Type 'credit', 'debit', or 'exit'.")
