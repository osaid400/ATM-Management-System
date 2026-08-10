import hashlib
from datetime import datetime, timedelta

class BankAccount:
    def __init__(self, name, account_number, balance, pin, transactions=None, is_active=True, failed_attempts=0, pin_is_hashed=False):
        self.__balance = float(balance)
        self.name = name
        self.account_number = int(account_number)
        self.is_active = is_active
        self.failed_attempts = int(failed_attempts)
        self._transactions = transactions or []

        pin_str = str(pin).strip()
        if pin_is_hashed:
            self.__pin_hash = pin_str
        else:
            self.__pin_hash = self._hash_pin(pin_str)

    @staticmethod
    def _hash_pin(pin_str):
        clean_pin = str(pin_str).zfill(4)
        return hashlib.sha256(clean_pin.encode("utf-8")).hexdigest()

    @property
    def balance(self):
        return self.__balance

    def check_active_status(self):
        if not self.is_active:
            raise ValueError("Account is FROZEN! Please contact bank administration.")

    def verify_pin(self, input_pin):
        self.check_active_status()

        if self._hash_pin(input_pin) == self.__pin_hash:
            self.failed_attempts = 0
            return True

        self.failed_attempts += 1
        if self.failed_attempts >= 3:
            self.is_active = False
            self.record_transaction("Account Frozen: 3 Failed PIN Attempts", 0)
            raise ValueError("Account FROZEN due to 3 consecutive wrong PIN attempts! Contact Admin.")

        remaining = 3 - self.failed_attempts
        raise ValueError(f"Incorrect PIN! Remaining attempts: {remaining}")

    def get_daily_withdrawn_amount(self):
        today = datetime.now().strftime("%Y-%m-%d")
        total = 0.0
        for tx in self._transactions:
            if tx.get("Date") == today and tx.get("Type") in ["Cash Withdrawal", "Transfer Sent"]:
                total += tx.get("Amount", 0.0)
        return total

    def record_transaction(self, transaction_type, amount):
        now = datetime.now()
        self._transactions.append({
            "Type": transaction_type,
            "Amount": float(amount),
            "Date": now.strftime("%Y-%m-%d"),
            "Time": now.strftime("%H:%M:%S")
        })

    def withdraw(self, amount):
        self.check_active_status()
        if amount <= 0:
            raise ValueError("Amount cannot be negative or zero!")
        if amount % 500 != 0:
            raise ValueError("Amount must be in multiples of Rs. 500 or Rs. 1,000!")
        if amount > self.__balance:
            raise ValueError("Insufficient balance in your account!")

        daily_spent = self.get_daily_withdrawn_amount()
        if daily_spent + amount > 50000:
            raise ValueError(f"Daily withdrawal limit of Rs. 50,000 exceeded! Used today: Rs. {daily_spent:,.2f}")

        self.__balance -= amount
        self.record_transaction("Cash Withdrawal", amount)

    def withdraw_for_transfer(self, amount):
        self.check_active_status()
        if amount <= 0:
            raise ValueError("Amount cannot be negative or zero!")
        if amount > self.__balance:
            raise ValueError("Insufficient balance in your account!")

        daily_spent = self.get_daily_withdrawn_amount()
        if daily_spent + amount > 50000:
            raise ValueError(f"Daily withdrawal limit of Rs. 50,000 exceeded! Used today: Rs. {daily_spent:,.2f}")

        self.__balance -= amount
        self.record_transaction("Transfer Sent", amount)

    def deposit_for_transfer(self, amount):
        self.check_active_status()
        self.__balance += amount
        self.record_transaction("Transfer Received", amount)

    def change_pin(self, old_pin, new_pin):
        self.check_active_status()
        self.verify_pin(old_pin)
        
        new_pin_str = str(new_pin).strip().zfill(4)
        if not new_pin_str.isdigit() or len(new_pin_str) != 4:
            raise ValueError("PIN must be exactly 4 digits!")

        self.__pin_hash = self._hash_pin(new_pin_str)
        self.record_transaction("PIN Changed", 0)

    def to_dict(self):
        return {
            "Holder_name": self.name,
            "Account_number": self.account_number,
            "Balance": self.__balance,
            "PIN_HASH": self.__pin_hash,
            "Is_Active": self.is_active,
            "Failed_Attempts": self.failed_attempts,
            "Transactions": self._transactions
        }

    @classmethod
    def from_dict(cls, account_data):
        pin_hash = account_data.get("PIN_HASH")
        is_active = account_data.get("Is_Active", True)
        failed_attempts = account_data.get("Failed_Attempts", 0)

        if pin_hash:
            return cls(
                name=account_data.get("Holder_name") or account_data.get("Name"),
                account_number=account_data.get("Account_number") or account_data.get("Account Number"),
                balance=account_data.get("Balance", 0.0),
                pin=pin_hash,
                transactions=account_data.get("Transactions", []),
                is_active=is_active,
                failed_attempts=failed_attempts,
                pin_is_hashed=True
            )

        raw_pin = str(account_data.get("PIN") or "1234")
        return cls(
            name=account_data.get("Holder_name") or account_data.get("Name"),
            account_number=account_data.get("Account_number") or account_data.get("Account Number"),
            balance=account_data.get("Balance", 0.0),
            pin=raw_pin,
            transactions=account_data.get("Transactions", []),
            is_active=is_active,
            failed_attempts=failed_attempts,
            pin_is_hashed=False
        )

    def statement(self, days=30):
        cutoff = datetime.now() - timedelta(days=days)
        recent_transactions = []
        for tx in self._transactions:
            try:
                tx_datetime = datetime.strptime(f"{tx['Date']} {tx['Time']}", "%Y-%m-%d %H:%M:%S")
                if tx_datetime >= cutoff:
                    recent_transactions.append(tx)
            except (KeyError, ValueError):
                continue
        return recent_transactions