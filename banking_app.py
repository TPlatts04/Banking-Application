class BalanceException(Exception):
    pass

class BankAccount():
    def __init__(self, name, amount) -> None:
        self.name = name
        self.balance = amount
        print(f"\nAccount under the name '{self.name}' has been created.\nThe balance of the account is £{self.balance:.2f}.")

    def viableBalanceAmount(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry there are insufficient funds within {self.name}'s account.")
        
    def getBalance(self):
        print(f"\n{self.name}'s current balance is: £{self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDepositing into {self.name}'s account...")
        print(f"\nBalance of {self.name}'s account is now: £{self.balance:.2f}")

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

class InterestAccount(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05) # Adds 5% interest to each deposit
        print(f"\nDepositing into {self.name}'s account...")
        print(f"\nBalance of {self.name}'s account is now: £{self.balance:.2f}")

class SavingsAccount(InterestAccount):
    def __init__(self, name, amount) -> None:
        super().__init__(name, amount)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableBalanceAmount(amount)
            print("\nAttempting withdrawal... 🔃")
            self.balance -= (amount + self.fee)
            print(f"\nWithdrawal of £{amount} completed. ✅")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdrawal interrupted: ❌ {error}")


