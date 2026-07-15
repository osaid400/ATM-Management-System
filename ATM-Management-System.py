
# ATM Management System
# Author: Muhammad Abdullah Farooq
# Language: Python
# Level: Beginner

import os
import json
import sys

print("============ Welcome to ATM Management System =============")

# ---------------- File Handling ----------------

def load_accounts():
    if os.path.exists("accounts.json"):
        with open("accounts.json", "r") as file:
            data = json.load(file)
        return data
    else:
        return []

def save_accounts():
    with open("accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)

accounts = load_accounts()

if not accounts:
    accounts = [
        {"Name" : "Ali", "Account Number": 3011, "PIN" : 1234, "Balance": 15000},
        {"Name" : "Abdullah", "Account Number": 3012, "PIN" : 3457, "Balance": 23000},
        {"Name" : "Sudies", "Account Number": 3013, "PIN" : 7456, "Balance": 19000},
        {"Name" : "Alina", "Account Number": 3014, "PIN" : 9345, "Balance": 1000},
        {"Name" : "Asghar", "Account Number": 3015, "PIN" : 9755, "Balance": 50000},
        {"Name" : "Bilal", "Account Number": 3016, "PIN" : 1245, "Balance": 13000},
        {"Name" : "Zayan", "Account Number": 3017, "PIN" : 6654, "Balance": 23000},
        {"Name" : "Zubair", "Account Number": 3018, "PIN" : 3321, "Balance": 35000},
    ]  
    save_accounts()

# ---------------- Functions ----------------

def check_balance(account):
    print(f"Current Balance: Rs. {account['Balance']:,}")

def deposit_money(account):
    try:
        amount = int(input("Enter Amount: "))
    except ValueError:
        print("Invalid Amount!")
        return

    if amount <= 0:
        print("Amount cannot be Negative or Zero!")
        return
    account["Balance"] += amount
    save_accounts()
    print("Money Deposited Successfully!")
    print(f"Current Balance: Rs. {account['Balance']:,}")

def withdraw_money(account):
    try:
        amount = int(input("Enter Amount: "))
    except ValueError:
        print("Invalid Amount!")
        return
    
    if amount <= 0:
        print("Invalid Amount!")
        return
    if amount > account ["Balance"]:
        print("Insufficient Balance!")
        return
    account["Balance"] -= amount
    save_accounts()
    print("Money Withdrawn Successfully!")
    print(f"Current Balance: Rs. {account['Balance']:,}")


def change_pin(account):
        try:
            old = int(input("Enter current PIN: "))
        except ValueError:
            print("Invalid PIN!")
            return

        if old != account["PIN"]:
            print("Incorrect PIN!")
            return

        try:
            new = int(input("Enter new PIN: "))
        except ValueError:
            print("Invalid PIN!")
            return

        if new == old:
            print("New PIN cannot be same as old PIN.")
            return
        
        if new <1000 or new >9999:
            print("PIN must be exactly 4 digits!")
            return

        account["PIN"] = new
        save_accounts()
        print("PIN changed successfully!")

def log_out():
    print("Logged out successfully.")

def log_in():
    try:
        account_number = int(input("Enter the Account number: "))
    except ValueError:
        print("Invalid Account Number!")
        return
    
    try:
        pin = int(input("Enter the pin: "))
    except ValueError:
        print("Invalid PIN Number")
        return

    for account in accounts:
        if account["Account Number"] == account_number and account["PIN"] == pin:
            print("Login Successful")
            return account
    print("Invalid Account Number or PIN.")
    return None

# ---------------- MENU's ----------------

def atm_menu(account):
    while True:
        print()
        print("=============== Select the Option ===============")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change Pin")
        print("5. Logout")
        print("0. Back to Main Menu")
        
        try:
            choice_2 = int(input("Enter the number: "))
        except ValueError:
            print("Invalid Choice!")
            continue

        if choice_2 == 1:
            check_balance(account)
        elif choice_2 == 2:
            deposit_money(account)
        elif choice_2 == 3:
            withdraw_money(account)
        elif choice_2 == 4:
            change_pin(account)
        elif choice_2 == 5:
            log_out()
            break
        elif choice_2 == 0:
            break
        else:
            print("Invalid Choice!")

while True:
    print()
    print("=============== Select the Option ===============")
    print("1. Login")
    print("0. Exit")

    try:
        choice = int(input("Enter the number: "))
    except ValueError:
        print("Invalid Choice!")
        continue

    if choice == 1:
        account = log_in()
        if account:
            atm_menu(account)
    elif choice == 0:
        print("Thank You for using our application :) ")
        print("Good Bye!")
        sys.exit()
    else:
        print("Invalid Choice!")

