import json
import hashlib
from pathlib import Path
from datetime import datetime
from src.models import BankAccount

class ATMManager:
    def __init__(self, filename="data/accounts.json", vault_file="data/vault.json"):
        self.filename = Path(filename)
        self.vault_file = Path(vault_file)
        self.accounts = []
        self.vault_balance = 200000.0
        self._receipt_counter = 0

        self.load_accounts()
        self.load_vault()

        if not self.accounts and not self.filename.exists():
            self.accounts = [
                BankAccount("Ali", 3011, 15000, "1234"),
                BankAccount("Abdullah", 3012, 23500, "1234"),
                BankAccount("Ahmed", 3013, 23500, "1234"),
                BankAccount("Zohaib", 3014, 55500, "1234"),
                BankAccount("Fabiha", 3015, 13500, "1234"),
            ]
            self.save_accounts()

    def admin_login(self, username, password):
        admin_user_hash = hashlib.sha256("admin".encode()).hexdigest()
        admin_pass_hash = hashlib.sha256("12345".encode()).hexdigest()

        input_user_hash = hashlib.sha256(username.strip().encode()).hexdigest()
        input_pass_hash = hashlib.sha256(password.strip().encode()).hexdigest()

        return input_user_hash == admin_user_hash and input_pass_hash == admin_pass_hash

    def load_accounts(self):
        if self.filename.exists():
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    self.accounts = [BankAccount.from_dict(item) for item in data]
            except (json.JSONDecodeError, ValueError, OSError):
                self.accounts = []

    def save_accounts(self):
        self.filename.parent.mkdir(parents=True, exist_ok=True)
        with open(self.filename, "w", encoding="utf-8") as file:
            data = [acc.to_dict() for acc in self.accounts]
            json.dump(data, file, indent=4)

    def load_vault(self):
        if self.vault_file.exists():
            try:
                with open(self.vault_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    self.vault_balance = float(data.get("vault_balance", 200000.0))
            except (json.JSONDecodeError, ValueError, OSError):
                self.vault_balance = 200000.0

    def save_vault(self):
        self.vault_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.vault_file, "w", encoding="utf-8") as file:
            json.dump({"vault_balance": self.vault_balance}, file, indent=4)

    def refill_vault(self, amount):
        if amount <= 0:
            raise ValueError("Refill amount must be positive.")
        self.vault_balance += amount
        self.save_vault()

    def unfreeze_account(self, account):
        account.is_active = True
        account.failed_attempts = 0
        account.record_transaction("Account Unfrozen by Admin", 0)
        self.save_accounts()

    def find_account(self, account_number):
        try:
            acc_num = int(account_number)
            return next((acc for acc in self.accounts if acc.account_number == acc_num), None)
        except ValueError:
            return None

    def dispense_cash(self, account, amount):
        if amount > self.vault_balance:
            raise ValueError("ATM Out of Cash! Please try a smaller amount or visit nearest branch.")

        account.withdraw(amount)
        self.vault_balance -= amount

        notes_1000 = int(amount // 1000)
        remaining = amount % 1000
        notes_500 = int(remaining // 500)

        self.save_accounts()
        self.save_vault()

        return {"1000": notes_1000, "500": notes_500}

    def transfer_money(self, sender_account, receiver_account, amount):
        sender_account.check_active_status()
        receiver_account.check_active_status()

        if amount <= 0:
            raise ValueError("Amount cannot be negative or zero!")
        if sender_account.account_number == receiver_account.account_number:
            raise ValueError("You cannot transfer money to your own account.")

        sender_account.withdraw_for_transfer(amount)
        receiver_account.deposit_for_transfer(amount)

        self.save_accounts()
        return True

    def generate_receipt(self, account, transaction_type, amount, description="", subfolder="general"):
        receipts_dir = Path("receipts") / subfolder
        receipts_dir.mkdir(parents=True, exist_ok=True)

        self._receipt_counter += 1
        file_name = f"{account.account_number}_TXN{self._receipt_counter:04d}.txt"
        receipt_path = receipts_dir / file_name

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
            f"Description    : {description or 'N/A'}",
            f"Current Balance: Rs. {account.balance:,.2f}",
            "=" * 60,
        ]
        receipt_path.write_text("\n".join(lines), encoding="utf-8")
        return receipt_path