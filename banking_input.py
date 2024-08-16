from banking_app import *
import os
import csv
import sys

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
tempList = []

def main():
    print("\nWelcome to Tom's Banking Application!")
    options = int(input("Would you like to:\n(1) Create an account\n(2) Deposit to the account\n(3) Withdraw from the account\n(4) Transfer to another account\n(5) To exit program.\nEnter option number here: "))
    match options:
        case 1:
            createAccount()
        case 2:
            depositAccount()
        case 3:
            withdrawAccount()
        case 4:
            transferAccount()
        case 5:
            sys.exit()
        case "_":
            print("Invalid option, please try again...")
            main()

def appendCSV():
    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file, fieldnames=CSV_FIELDNAMES)
        loopCounter = 0
        for row in reader:
            if row["account_name"] != "account_name":
                accountHolder = BankAccount(row["account_name"], float(row["balance"]))
                accounts.append(accountHolder)
                os.system('cls')
            else:
                loopCounter += 1
                if loopCounter == len(row):
                    main()
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
    accountType = int(input("What type of account would you like to open?\n(1) Regular Bank Account\n(2) Interest Rewards Account\n(3) Savings Account:\nEnter option number here:"))
    match accountType:
        case 1:
            accountName = input("\nWhat is the to be Account Holder's name? ").capitalize()
            for names in accounts:
                if (names.name) == accountName:
                    print("Account name already exists. Please try again...")
                    createAccount()
            accountInitialDeposit = int(input("\nHow much would you like to initally deposit into the account? £"))
            accountHolder = BankAccount(accountName, accountInitialDeposit)
            accounts.append(accountHolder)
        case 2:
            accountName = input("\nWhat is the to be Account Holder's name? ").capitalize()
            for names in accounts:
                if (names.name) == accountName:
                    print("Account name already exists. Please try again...")
                    createAccount()
            accountInitialDeposit = int(input("\nHow much would you like to initally deposit into the account? £"))
            accountHolder = InterestAccount(accountName, accountInitialDeposit)
            accounts.append(accountHolder)
        case 3:
            accountName = input("\nWhat is the to be Account Holder's name? ").capitalize()
            for names in accounts:
                if (names.name) == accountName:
                    print("Account name already exists. Please try again...")
                    createAccount()
            accountInitialDeposit = int(input("\nHow much would you like to initally deposit into the account? £"))
            accountHolder = SavingsAccount(accountName, accountInitialDeposit)
            accounts.append(accountHolder)
    with open(FILENAME, "a") as file:
        file.writelines(f"{accountName},{accountInitialDeposit}\n")
    main()

def depositAccount():
    loopCounter = 0
    depositLocation = input("\nWhat account would you like to send this deposit to?\n(Enter name of account holder): ").capitalize()
    for names in accounts:
        if names.name == depositLocation:
            depositAmount = float(input(f"\nHow much would you like to deposit in {depositLocation}'s account? £"))
            names.deposit(depositAmount)
            names.getBalance()
            with open(FILENAME, "r") as file:
                lines = file.readlines()
                indexOfLine = 0
                for x in range(len(lines)):
                    if depositLocation in lines[x].strip().replace(",", " "):
                        indexOfLine = x
                lines[indexOfLine] = f"{names.name},{names.balance}\n"
            with open(FILENAME, "w") as file:
                file.writelines(lines)
            main()
        else:
            loopCounter += 1
            if loopCounter == len(accounts):
                print("Invalid name, try again")
                depositAccount()
        

def withdrawAccount():
    loopCounter = 0
    withdrawLocation = input("\nWhich account would you like to withdraw from?\n(Enter name of account holder): ").capitalize()
    for names in accounts:
        if names.name == withdrawLocation:
            withdrawAmount = float(input("\bHow much would you like to withdraw? £"))
            names.withdraw(withdrawAmount)
            with open(FILENAME, "r") as file:
                lines = file.readlines()
                indexOfLine = 0
                for x in range(len(lines)):
                    if withdrawLocation in lines[x].strip().replace(",", " "):
                        indexOfLine = x
                lines[indexOfLine] = f"{names.name},{names.balance}\n"
            with open(FILENAME, "w") as file:
                file.writelines(lines)
            main()
        else:
            loopCounter += 1
            if loopCounter == len(accounts):
                print("Invalid user, try again")
                depositAccount()

def transferAccount():
    transferStart = input("\nWhich account would you like to transfer from?\n(Enter name of account holder): ").capitalize()
    transferEnd = input("\nWhich account would you like to transfer to?\n(Enter name of account holder): ").capitalize()
    loopCounter = 0
    for nameStart in accounts:
        if nameStart.name == transferStart:
            for nameEnd in accounts:
                if nameEnd.name == transferEnd:
                    transferAmount = float(input(f"\nHow much would you like to transfer to {transferEnd}'s account? £"))
                    nameStart.transfer(transferAmount, nameEnd)
                    with open(FILENAME, "r") as file:
                        lines = file.readlines()
                        indexOfLine = 0
                        for x in range(len(lines)):
                            if transferStart in lines[x].strip().replace(",", " "):
                                indexOfLine = x
                        lines[indexOfLine] = f"{nameStart.name},{nameStart.balance}\n"
                        for y in range(len(lines)):
                            if transferEnd in lines[y].strip().replace(",", " "):
                                indexOfLine = y
                        lines[indexOfLine] = f"{nameEnd.name},{nameEnd.balance}\n"
                    with open(FILENAME, "w") as file:
                        file.writelines(lines)
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
        appendCSV()
    else:
        f = open(FILENAME, "w")
        f.write("account_name,balance\n")
        f.close()
        assignFieldnames()
        appendCSV()