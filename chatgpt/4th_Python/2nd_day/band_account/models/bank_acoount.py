class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit  of ${amount:.2f} completed.")
        else:
            print("The deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("The withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insuficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount:2f} completed.")

    def check_balance(self):
        print(f"Account owner: {self.owner}")
        print(f"Balance: ${self.balance:.2f}")
        