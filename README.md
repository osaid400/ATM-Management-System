# ATM Management System

A console-based **ATM Management System** built with Python. This project simulates the core functionality of an Automated Teller Machine (ATM) while demonstrating Object-Oriented Programming (OOP), encapsulation, JSON-based data persistence, authentication, transaction logging, input validation, modular design, and exception handling.

## Features

* Login using Account Number and 4-digit PIN
* Secure PIN authentication
* Check account balance
* Deposit money
* Withdraw money
* Change account PIN
* View 30-day cash statement
* Mini statement printing (Last 5 transactions)
* Transfer money between accounts
* Automated receipt generation (Saved in `receipts/` subfolders)
* Automatic transaction logging with date and time
* Persistent storage using JSON
* Input validation and exception handling
* Logout functionality

## Technologies Used

* Python 3
* JSON

## Concepts Covered

* Object-Oriented Programming (OOP)
* Classes and Objects
* Modular Architecture & Package Structuring
* Encapsulation (`private attributes`)
* Properties (`@property`)
* Class Methods (`@classmethod`)
* Static Methods (`@staticmethod`)
* Lists and Dictionaries
* JSON File Handling
* File Persistence
* Date & Time (`datetime`)
* Loops
* Conditional Statements
* Exception Handling
* Input Validation
* Menu-Driven Programming

## Project Structure

```text
ATM-Management-System/
│
├── data/
│   └── accounts.json         # Persistent JSON account records
│
├── receipts/                 # Auto-generated transaction receipts
│   ├── general/
│   ├── received/
│   └── sent/
│       └── .gitkeep
│
├── src/                      # Source code modules
│   ├── __init__.py
│   ├── models.py             # BankAccount data model & methods
│   ├── manager.py            # ATMManager business & persistence logic
│   └── UI.py                 # CLI menus and display formatting
│
├── .gitignore                # Excludes pycache, receipts, and local data
├── main.py                   # Application entry point
└── README.md                 # Project documentation

```

> **Note:** `data/accounts.json` is created automatically when the program is first executed. It stores account information and transaction history locally and is excluded from the repository using `.gitignore`.

## Default Sample Accounts

| Account Holder | Account Number | PIN |
| --- | --- | --- |
| Ali | 3011 | 4321 |
| Abdullah | 3012 | 4321 |
| Ahmed | 3013 | 1234 |
| Zohaib | 3014 | 1234 |
| Fabiha | 3015 | 1234 |
| Rida | 3016 | 1234 |
| Asghar | 3017 | 1234 |
| Zayan | 3018 | 1234 |
| Akshay Kumar | 3019 | 1234 |
| Obaid | 3020 | 1234 |

## How to Run

1. Clone the repository:

```bash
git clone [https://github.com/osaid400/ATM-Management-System.git](https://github.com/osaid400/ATM-Management-System.git)

```

2. Navigate to the project folder:

```bash
cd ATM-Management-System

```

3. Run the program:

```bash
python main.py

```

## Example Output

### Login

```text
============================================================
              WELCOME TO ATM MANAGEMENT SYSTEM              
============================================================

1. Login
0. Exit
------------------------------------------------------------

Enter choice: 1

Enter Account Number: 3012
Enter 4-digit PIN: 4321

Login Successful!

```

### ATM Menu

```text
============================================================
                     Welcome Back, Abdullah                     
============================================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Change Pin
5. Cash Statement (30 Days)
6. Transfer Money
7. Mini Statement
8. Logout
0. Back to Main Menu
------------------------------------------------------------
Enter choice: 

```

### Deposit

```text
Enter Amount to Deposit: 5000

Deposit Successful! Balance: Rs. 27,500.00
Receipt saved to: receipts/general/3012_TXN0001.txt

```

### Withdraw

```text
Enter Amount to Withdraw: 2500

Withdrawal Successful! Balance: Rs. 25,000.00
Receipt saved to: receipts/general/3012_TXN0002.txt

```

### Change PIN

```text
Enter current PIN: 4321
Enter new PIN: 9876

PIN changed successfully!

```

### Transfer Money

```text
Enter recipient account number: 3011
Enter transfer amount: 1000

Money Transferred Successfully!

```

### Cash Statement

```text
============================================================
         30-Day Cash Statement for Abdullah (3012)
============================================================
Current Balance: Rs. 22,500.00
Last 30 days transactions:
------------------------------------------------------------
Date         Time       Type                 Amount
------------------------------------------------------------
2026-07-28   09:44:43   Withdrawal      Rs.     500.00
2026-08-07   08:52:04   Transfer Sent   Rs.   1,000.00
2026-08-07   09:00:09   Transfer Rec.   Rs.     500.00
============================================================

```

### Mini Statement

```text
============================================================
Mini Statement for Abdullah (3012)
============================================================
Current Balance: Rs. 22,500.00
2026-08-07 09:00:09 | Transfer Rec.   | Rs. 500.00
2026-08-07 08:52:04 | Transfer Sent   | Rs. 1,000.00
2026-07-28 09:44:43 | Withdrawal      | Rs. 500.00
============================================================

```

## How Data Persistence Works

* On startup, the program checks whether `data/accounts.json` exists.
* If the file exists, all account data is loaded automatically.
* If it doesn't exist, default sample accounts are created.
* Every deposit, withdrawal, PIN change, transfer, or other account update is immediately saved to `data/accounts.json`.
* Every transaction is recorded with its **type, amount, date, and time**, allowing the program to generate a 30-day cash statement and mini statement.
* Transaction receipts are automatically generated and structured in designated folders under `receipts/`.

## Future Improvements

* Three-attempt PIN lock system
* ATM cash withdrawal denominations logic
* Password hashing for PIN security (e.g., using `bcrypt` or `argon2`)
* Account locking mechanism after multiple invalid login attempts
* SQLite or PostgreSQL database integration replacing JSON persistence
* RESTful API backend implementation (using FastAPI / Flask)
* Graphical User Interface (GUI using PyQt or CustomTkinter)
* Multi-currency support and live exchange rate conversion

## Learning Outcomes

This project helped me practice:

* Designing applications using Object-Oriented Programming
* Structuring code into scalable Python modules (Models, Managers, UI)
* Implementing encapsulation with private attributes
* Creating reusable classes and methods
* Managing persistent data with JSON
* Recording transaction history and generating text receipts
* Working with dates and times using `datetime`
* Implementing secure user authentication
* Validating user input and handling exceptions
* Building a complete menu-driven console application

## Author

**Osaid**

GitHub: https://github.com/osaid400

```
