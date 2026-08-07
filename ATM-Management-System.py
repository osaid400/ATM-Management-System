# ==========================================
# ATM MANAGEMENT SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python 3.13
# =========================================== 

import os
import json
import sys
from pathlib import Path
from datetime import datetime, timedelta

class Bank_Account():
    def __init__(self, name, account_number, balance, pin, transactions=None):
        self.__balance = float(balance)
        self.__pin = str(pin).zfill(4)
        self.name = name
        self.account_number = account_number
        self.__transactions = transactions or []

    @property
    def balance(self):
        return self.__balance

    def verify_pin(self, input_pin):
        return str(input_pin).zfill(4) == self.__pin

    def record_transaction(self, transaction_type, amount):
        now = datetime.now()
        self.__transactions.append({
            "Type": transaction_type,
            "Amount": float(amount),
            "Date": now.strftime("%Y-%m-%d"),
            "Time": now.strftime("%H:%M:%S")
        })

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount cannot be negative or zero!")
        self.__balance += amount
        self.record_transaction("Deposit", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount cannot be negative or zero!")
        if amount > self.__balance:
            raise ValueError("Insufficient Balance!")
        self.__balance -= amount
        self.record_transaction("Withdrawal", amount)

    def change_pin(self, old_pin, new_pin):
        if not self.verify_pin(old_pin):
            raise ValueError("Incorrect current PIN!")

        self.record_transaction("PIN Changed", 0)

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
            "PIN": self.__pin,
            "Transactions": self.__transactions
        }

    @classmethod
    def from_dict(cls, account_data):
        return cls(
            name=account_data.get("Holder_name") or account_data.get("Name"),
            account_number=account_data.get("Account_number") or account_data.get("Account Number"),
            balance=account_data.get("Balance", 0),
            pin=str(account_data.get("PIN", "1234")),
            transactions=account_data.get("Transactions", [])
        )

    def statement(self, days=30):
        cutoff = datetime.now() - timedelta(days=days)
        recent_transactions = []

        for tx in self.__transactions:
            try:
                tx_datetime = datetime.strptime(f"{tx['Date']} {tx['Time']}", "%Y-%m-%d %H:%M:%S")
            except (KeyError, ValueError):
                continue

            if tx_datetime >= cutoff:
                recent_transactions.append(tx)

        return recent_transactions

class ATM_Manager():    

    def __init__(self, filename="accounts.json"):
        self.filename = filename
        self.accounts = []
        self._receipt_counter = 0
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
        pin = input("Enter 4-digit PIN: ").strip()
        if not account.verify_pin(pin):
            print("Incorrect PIN!")
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
        receipt_path = self.generate_receipt(account, "Deposit", amount, "Cash Deposit")
        print("Money Deposited Successfully!")
        print(f"Current Balance: Rs. {account.balance:,.2f}")
        print(f"Receipt saved to: {receipt_path}")

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
        receipt_path = self.generate_receipt(account, "Withdrawal", amount, "Cash Withdrawal")
        print("Money Withdrawn Successfully!")
        print(f"Current Balance: Rs. {account.balance:,.2f}")
        print(f"Receipt saved to: {receipt_path}")

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

    def cash_statement(self, account):
        statement = account.statement(days=30)
        print()
        print("=" * 60)
        print(f"         30-Day Cash Statement for {account.name} ({account.account_number})")
        print("=" * 60)
        print(f"Current Balance: Rs. {account.balance:,.2f}")
        print("Last 30 days transactions:")
        print("-" * 60)

        if not statement:
            print("No deposits or withdrawals found in the last 30 days.")
            print("=" * 60)
            return

        header = f"{'Date':<12} {'Time':<10} {'Type':<12} {'Amount':>14}"
        print(header)
        print("-" * 60)

        for tx in statement:
            tx_type = tx.get("Type", "Unknown")
            amount = tx.get("Amount", 0.0)
            date = tx.get("Date", "----/--/--")
            time = tx.get("Time", "--:--:--")
            print(f"{date:<12} {time:<10} {tx_type:<12} Rs. {amount:>10,.2f}")

        print("=" * 60)
        print("End of Statement")
        print("=" * 60)

    def ensure_receipts_directory(self, subfolder="general"):
        receipts_dir = Path(__file__).resolve().parent / "receipts"
        target_dir = receipts_dir / subfolder if subfolder else receipts_dir
        target_dir.mkdir(parents=True, exist_ok=True)
        return target_dir

    def next_receipt_id(self):
        self._receipt_counter += 1
        return self._receipt_counter

    def generate_receipt(self, account, transaction_type, amount, description="", subfolder="general", transaction_id=None):
        receipts_dir = self.ensure_receipts_directory(subfolder)
        receipt_id = transaction_id if transaction_id is not None else self.next_receipt_id()
        file_name = f"{account.account_number}_TXN{receipt_id:04d}.txt"
        receipt_path = receipts_dir / file_name

        balance = account.balance
        lines = [
            "=" * 60,
            "ATM MANAGEMENT SYSTEM - RECEIPT".center(60),
            "=" * 60,
            f"Account Holder : {account.name}",
            f"Account Number : {account.account_number}",
            f"Date           : {datetime.now().strftime('%Y-%m-%d')}",
            f"Time           : {datetime.now().strftime('%H:%M:%S')}",
            f"Transaction    : {transaction_type}",
            f"Amount         : Rs. {float(amount):,.2f}",
            f"Description    : {description or 'No description provided'}",
            f"Current Balance: Rs. {balance:,.2f}",
            "=" * 60,
            "Thank you for banking with us!"
        ]

        receipt_path.write_text("\n".join(lines), encoding="utf-8")
        return f"receipts/{subfolder}/{file_name}"

    def get_mini_statement(self, account, limit=5):
        transactions = list(reversed(account._Bank_Account__transactions))
        return transactions[:limit]

    def print_mini_statement(self, account, limit=5):
        transactions = self.get_mini_statement(account, limit)
        print()
        print("=" * 60)
        print(f"Mini Statement for {account.name} ({account.account_number})")
        print("=" * 60)
        print(f"Current Balance: Rs. {account.balance:,.2f}")
        if not transactions:
            print("No transactions recorded yet.")
            print("=" * 60)
            return

        for tx in transactions:
            tx_type = tx.get("Type", "Unknown")
            amount = tx.get("Amount", 0.0)
            date = tx.get("Date", "----/--/--")
            time = tx.get("Time", "--:--:--")
            print(f"{date} {time} | {tx_type:<15} | Rs. {amount:,.2f}")
        print("=" * 60)

    def transfer_money(self, sender_account, receiver_account, amount=None):
        if amount is None:
            try:
                amount = float(input("Enter Amount: "))
            except ValueError:
                print("Invalid Amount!")
                return False

        if amount <= 0:
            print("Amount cannot be Negative or Zero!")
            return False

        if sender_account.account_number == receiver_account.account_number:
            print("You cannot transfer money to your own account.")
            return False

        if sender_account.balance < amount:
            print("Insufficient balance for this transfer.")
            return False

        sender_account._Bank_Account__balance -= amount
        receiver_account._Bank_Account__balance += amount
        sender_account.record_transaction("Transfer Sent", amount)
        receiver_account.record_transaction("Transfer Received", amount)
        self.save_accounts()

        transaction_id = self.next_receipt_id()
        sender_receipt = self.generate_receipt(sender_account, "Transfer Sent", amount, f"To {receiver_account.name}", subfolder="sent", transaction_id=transaction_id)
        receiver_receipt = self.generate_receipt(receiver_account, "Transfer Received", amount, f"From {sender_account.name}", subfolder="received", transaction_id=transaction_id)
        print("Money transferred successfully!")
        print(f"Current Balance: Rs. {sender_account.balance:,.2f}")
        print(f"Receipt saved to: {sender_receipt}")
        print(f"Receipt saved to: {receiver_receipt}")
        return True

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
        print("=" * 60)
        print(f"Welcome Back, {account.name}".center(60))
        print("=" * 60)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change Pin")
        print("5. Last 30 days Cash Statement")
        print("6. Transfer Money")
        print("7. Bank Statement")
        print("8. Logout")
        print("0. Back to Main Menu")
        print("-" * 60)
        
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
            receiver_number = int(input("Enter recipient account number: "))
            receiver_account = manager.find_account(receiver_number)
            if receiver_account is None:
                print("Recipient account not found.")
                continue
            manager.transfer_money(account, receiver_account)
        elif choice_2 == 7:
            manager.print_mini_statement(account)
        elif choice_2 == 8:
            manager.log_out()
            break
        elif choice_2 == 0:
            break
        else:
            print("Invalid Choice!")

atm_manager = ATM_Manager()

while True:

    print("=" * 60)
    print("WELCOME TO ATM MANAGEMENT SYSTEM".center(60))
    print("=" * 60)
    print("1. Login")
    print("0. Exit")
    print("-" * 60)

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

