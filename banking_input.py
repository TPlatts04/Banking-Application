from banking_app import *
import os
import csv

# Testing
# Tom = BankAccount("Tom", 500)
# Tom.deposit(350)
# Tom.withdraw(10000)
# Tom.withdraw(250)

# Ismail = BankAccount("Ismail", 600)
# Tom.transfer(200, Ismail)
# Tom.transfer(1000, Ismail)

# Storm = InterestAccount("Storm", 1000)
# Storm.deposit(100)

# Josh = SavingsAccount("Josh", 2000)
# Josh.withdraw(10000)
# Josh.withdraw(1000)

FILENAME = "bank_data.csv"
CSV_FIELDNAMES = []

accounts = []

def main():
    print("\nWelcome to Tom's Banking Application!")
    options = int(input("Would you like to\n(1) Create an account\n(2) Deposit to the account\n(3) Withdraw from the account\n(4) Transfer to another account\nEnter option number here: "))
    match options:
        case 1:
            createAccount()
        case 2:
            depositAccount()
        case 3:
            withdrawAccount()
        case 4:
            transferAccount()
        case "_":
            print("Invalid option, please try again...")
            main()

def assignFieldnames():
    with open(FILENAME, "r") as file:
        lines = file.readlines()
        i = 0
        while i < 1:
            CSV_FIELDNAMES.extend(lines[0].strip().split(","))
            i+=1

def createAccount():
    global newAccount
    accountName = input("\nWhat is the to be Account Holder's name? ")
    accountInitialDeposit = int(input("\nHow much would you like to initally deposit into the account? £"))
    accountHolder = BankAccount(accountName, accountInitialDeposit)
    accounts.append(accountHolder)
    print(accounts)
    main()

def depositAccount():
    depositLocation = input("\nWhat account would you like to send this deposit to?\n(Enter name of account holder): ")
    for names in accounts:
        if names.name == depositLocation:
            depositAmount = float(input(f"\nHow much would you like to deposit in {depositLocation}'s account? £"))
            names.deposit(depositAmount)
            names.getBalance()
            main()
        else:
            print("Invalid name, try again")
            depositAccount()
        

def withdrawAccount():
    withdrawLocation = input("\nWhich account would you like to withdraw from?\n(Enter name of account holder): ")
    for names in accounts:
        if names.name == withdrawLocation:
            withdrawAmount = float(input("\bHow much would you like to withdraw? £"))
            names.withdraw(withdrawAmount)
            main()
        else:
            print("Invalid user, try again...")
            withdrawAccount()

def transferAccount():
    transferStart = input("\nWhich account would you like to transfer from?\n(Enter name of account holder): ")
    transferEnd = input("\nWhich account would you like to transfer to?\n(Enter name of account holder): ")
    loopCounter = 0
    for nameStart in accounts:
        if nameStart.name == transferStart:
            for nameEnd in accounts:
                if nameEnd.name == transferEnd:
                    transferAmount = float(input(f"\nHow much would you like to transfer to {transferEnd}'s account? £"))
                    nameStart.transfer(transferAmount, nameEnd)
                    main()
                else:
                    loopCounter += 1
                    if loopCounter == len(accounts):
                        print("Invalid second user, try again...")
                        transferAccount()
        else:
            loopCounter += 1
            if loopCounter == len(accounts):
                print("Invalid first user, try again...")
                transferAccount()

if __name__ == "__main__":
    if os.path.isfile(FILENAME):
        assignFieldnames()
        main()
    else:
        f = open(FILENAME, "w")
        f.write("account_name,balance\n")
        f.close()
        assignFieldnames()
        main()