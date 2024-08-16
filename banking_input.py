from banking_app import *

# Testing
Tom = BankAccount("Tom", 500)
Tom.deposit(350)
Tom.withdraw(10000)
Tom.withdraw(250)

Ismail = BankAccount("Ismail", 600)
Tom.transfer(200, Ismail)
Tom.transfer(1000, Ismail)