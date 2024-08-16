class BalanceException(Exception):
    pass

class BankAccount():
    def __init__(self, name, amount) -> None:
        self.name = name
        self.balance = amount
        print(f"\nAccount under the name '{self.name}' has been created.\nThe balance of the account is £{self.balance}.")

    def viableBalanceAmount(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry there are insufficient funds within {self.name}'s account.")
        
    def getBalance(self):
        print(f"\n{self.name}'s current balance is: £{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nBalance of {self.name}'s account is now: £{self.balance}")

    def withdraw(self, amount):
        try:
            print("\nAttempting withdrawal... 🔃")
            self.viableBalanceAmount(amount)
            self.balance -= amount
            print(f"\nWithdrawal of £{amount} completed. ✅")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdrawal interrupted: ❌ {error}")

    def transfer(self, amount, account):
        try:
            print("\nAttempting transfer... 🔃")
            self.viableBalanceAmount(amount)
            self.balance -= amount
            print(f"\nTransfer of £{amount} completed. ✅")
            account.deposit(amount)
            self.getBalance()
        except BalanceException as error:
            print(f"\nTransfer interrupted: ❌ {error}")
