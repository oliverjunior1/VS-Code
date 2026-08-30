class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Customer(Person):
    def __init__(self, firstname, lastname, account_number, balance):
        super().__init__(firstname, lastname)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, value):
        self.balance += value
        print(f"Deposit successful! New balance: {self.balance}")

    def withdraw(self, value):
        if self.balance - value < 0:
            print("Your balance isn't enough to withdraw, put another value!")
        else:
            self.balance -= value
            print(f"Withdraw successful! New balance: {self.balance}")

    def exit(self):
        print("Exiting account... Goodbye!")

# Exemplo de uso
cliente = Customer("Maria", "Silva", "12345", 500)

cliente.deposit(200)   # +200 → saldo 700
cliente.withdraw(100)  # -100 → saldo 600
cliente.withdraw(700)  # saldo insuficiente
cliente.exit()

    

