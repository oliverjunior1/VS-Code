from models.bank_acoount import BankAccount

account1 = BankAccount("Mary", 500.00)

account1.check_balance()

account1.deposit(200.00)
account1.withdraw(150.00)

print("\nAfter the transaction:")
account1.check_balance()

account1.withdraw(1000.00)