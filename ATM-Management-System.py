
# ATM MANAGEMENT SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python
# Level: Beginner

import os
import json
import sys

print("============ Welcome to ATM Management System =============")

class Bank_Account():
    def __init__(self, name, account_number, balance, pin):
        self.__balance = float(balance)
        self.__pin = str(pin).zfill(4)
        self.name = name
        self.account_number = account_number

    @property
    def balance(self):
        return self.__balance

    def verify_pin(self, input_pin):
        return str(input_pin).zfill(4) == self.__pin

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount cannot be negative or zero!")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount cannot be negative or zero!")
        if amount > self.__balance:
            raise ValueError("Insufficient Balance!")
        self.__balance -= amount

    def change_pin(self, old_pin, new_pin):
        if not self.verify_pin(old_pin):
            raise ValueError("Incorrect current PIN!")

        new_pin_str = str(new_pin).zfill(4)
        if not new_pin_str.isdigit() or len(new_pin_str) != 4:
            raise ValueError("PIN must be exactly 4 digits!")

        self.__pin = new_pin_str

    def __str__(self):
        return (
            f"Account Holder: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance       : {self.__balance:.2f}"
        )

    def to_dict(self):
        return {
            "Holder_name": self.name,
            "Account_number": self.account_number,
            "Balance": self.__balance,
            "PIN": self.__pin
        }

    @classmethod
    def from_dict(cls, account_data):
        return cls(
            name=account_data.get("Holder_name") or account_data.get("Name"),
            account_number=account_data.get("Account_number") or account_data.get("Account Number"),
            balance=account_data.get("Balance", 0),
            pin=str(account_data.get("PIN", "1234"))
        )


class ATM_Manager():    

    def __init__(self, filename="accounts.json"):
        self.filename = filename
        self.accounts = []
        self.load_accounts()

        if not self.accounts:
            self.accounts = [
                Bank_Account("Ali", 3011, 15000, "1234"),
                Bank_Account("Abdullah", 3012, 23500, "1234"),
                Bank_Account("Ahmed", 3013, 23500, "1234"),
                Bank_Account("Zohaib", 3014, 55500, "1234"),
                Bank_Account("Fabiha", 3015, 13500, "1234"),
                Bank_Account("Rida", 3016, 52000, "1234"),
                Bank_Account("Asghar", 3017, 32500, "1234"),
                Bank_Account("Zayan", 3018, 76500, "1234"),
                Bank_Account("Akshay Kumar", 3019, 40000, "1234"),
                Bank_Account("Obaid", 3020, 45000, "1234"),
            ]
            self.save_accounts()

    def load_accounts(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    self.accounts = [Bank_Account.from_dict(item) for item in data]
            except (json.JSONDecodeError, ValueError, OSError):
                self.accounts = []
        else:
            self.accounts = []

    def save_accounts(self):
        with open(self.filename, "w") as file:
            data = [account.to_dict() for account in self.accounts]
            json.dump(data, file, indent=4)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def authenticate(self, account):
        pin_input = input("Enter 4-digit PIN: ").strip()

        if not pin_input.isdigit() or len(pin_input) != 4:
            print("Invalid PIN format! PIN must contain exactly 4 digits.")
            return False

        if not account.verify_pin(pin_input):
            print("Incorrect PIN! Access Denied.")
            return False

        return True

    def check_balance(self, account):
        print(f"Current Balance: Rs. {account.balance:,.2f}")
 
    def deposit_money(self, account):
        try:
            amount = float(input("Enter Amount: "))
        except ValueError:
            print("Invalid Amount!")
            return

        if amount <= 0:
            print("Amount cannot be Negative or Zero!")
            return

        account.deposit(amount)
        self.save_accounts()
        print("Money Deposited Successfully!")
        print(f"Current Balance: Rs. {account.balance:,.2f}")

    def withdraw_money(self, account):
        try:
            amount = float(input("Enter Amount: "))
        except ValueError:
            print("Invalid Amount!")
            return
    
        if amount <= 0:
            print("Invalid Amount!")
            return
        try:
            account.withdraw(amount)
        except ValueError as exc:
            print(exc)
            return

        self.save_accounts()
        print("Money Withdrawn Successfully!")
        print(f"Current Balance: Rs. {account.balance:,.2f}")

    def change_pin(self, account):
        old_pin = input("Enter current PIN: ").strip()
        if not old_pin.isdigit() or len(old_pin) != 4:
            print("Invalid PIN!")
            return

        new_pin = input("Enter new PIN: ").strip()
        if not new_pin.isdigit() or len(new_pin) != 4:
            print("PIN must be exactly 4 digits!")
            return

        if new_pin == old_pin:
            print("New PIN cannot be same as old PIN.")
            return

        try:
            account.change_pin(old_pin, new_pin)
        except ValueError as exc:
            print(exc)
            return

        self.save_accounts()
        print("PIN changed successfully!")

    def cash_statement(self):


    @staticmethod
    def log_out():
        print("Logged out successfully.")

    def log_in(self):
        try:
            account_number = int(input("Enter the Account number: "))
        except ValueError:
            print("Invalid Account Number!")
            return None
    
        pin = input("Enter the pin: ").strip()
        if not pin.isdigit() or len(pin) != 4:
            print("Invalid PIN Number")
            return None

        for account in self.accounts:
            if account.account_number == account_number and account.verify_pin(pin):
                print("Login Successful")
                return account

        print("Invalid Account Number or PIN.")
        return None

def atm_menu(manager, account):
    while True:
        print()
        print("=============== Select the Option ===============")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change Pin")
        print("5. Cash Statement")
        print("6. Logout")
        print("0. Back to Main Menu")
        
        try:
            choice_2 = int(input("Enter the number: "))
        except ValueError:
            print("Invalid Choice!")
            continue

        if choice_2 == 1:
            manager.check_balance(account)
        elif choice_2 == 2:
            manager.deposit_money(account)
        elif choice_2 == 3:
            manager.withdraw_money(account)
        elif choice_2 == 4:
            manager.change_pin(account)
        elif choice_2 == 5:
            manager.cash_statement(account)
        elif choice_2 == 6:
            manager.log_out()
            break
        elif choice_2 == 0:
            break
        else:
            print("Invalid Choice!")

atm_manager = ATM_Manager()

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
        account = atm_manager.log_in()
        if account:
            atm_menu(atm_manager, account)
    elif choice == 0:
        print("Thank You for using our application :) ")
        print("Good Bye!")
        sys.exit()
    else:
        print("Invalid Choice!")

