# ATM Management System

A console-based **ATM Management System** built with Python. This project simulates the core functionality of an Automated Teller Machine (ATM) while demonstrating Object-Oriented Programming (OOP), encapsulation, JSON-based data persistence, authentication, transaction logging, input validation, and exception handling.

## Features

* Login using Account Number and 4-digit PIN
* Secure PIN authentication
* Check account balance
* Deposit money
* Withdraw money
* Change account PIN
* View 30-day cash statement
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
├── ATM Management System.py
├── .gitignore
└── README.md
```

> **Note:** `accounts.json` is created automatically when the program is first executed. It stores account information and transaction history locally and is excluded from the repository using `.gitignore`.

## Default Sample Accounts

| Account Holder | Account Number |  PIN |
| -------------- | -------------: | ---: |
| Ali            |           3011 | 4321 |
| Abdullah       |           3012 | 4321 |
| Ahmed          |           3013 | 1234 |
| Zohaib         |           3014 | 1234 |
| Fabiha         |           3015 | 1234 |
| Rida           |           3016 | 1234 |
| Asghar         |           3017 | 1234 |
| Zayan          |           3018 | 1234 |
| Akshay Kumar   |           3019 | 1234 |
| Obaid          |           3020 | 1234 |

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/osaid400/ATM-Management-System.git
```

2. Navigate to the project folder:

```bash
cd ATM-Management-System
```

3. Run the program:

```bash
python "ATM Management System.py"
```

## Example Output

### Login

```text
============ Welcome to ATM Management System ============

1. Login
0. Exit

Enter the number: 1

Enter the Account Number: 3012
Enter the PIN: 1234

Login Successful
```

### ATM Menu

```text
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Change PIN
5. Cash Statement
6. Logout
0. Back to Main Menu
```

### Deposit

```text
Enter Amount: 5000

Money Deposited Successfully!

Current Balance: Rs. 28,500.00
```

### Withdraw

```text
Enter Amount: 2500

Money Withdrawn Successfully!

Current Balance: Rs. 26,000.00
```

### Change PIN

```text
Enter Current PIN: 1234
Enter New PIN: 9876

PIN Changed Successfully!
```

### Cash Statement

```text
============================================================
30-Day Cash Statement

Current Balance: Rs. 26,000.00

Date         Time       Type            Amount
------------------------------------------------------------
2026-07-28   14:15:30   Deposit         Rs. 5,000.00
2026-07-28   14:18:12   Withdrawal      Rs. 2,500.00
2026-07-28   14:22:41   PIN Changed     Rs. 0.00
============================================================
```

## How Data Persistence Works

* On startup, the program checks whether `accounts.json` exists.
* If the file exists, all account data is loaded automatically.
* If it doesn't exist, default sample accounts are created.
* Every deposit, withdrawal, PIN change, or other account update is immediately saved to `accounts.json`.
* Every transaction is recorded with its **type, amount, date, and time**, allowing the program to generate a 30-day cash statement.

## Future Improvements

* Transfer money between accounts
* Three-attempt PIN lock system
* ATM cash withdrawal denominations
* Mini statement printing
* Admin panel
* SQLite database integration
* Password hashing for PIN security
* Receipt generation

## Learning Outcomes

This project helped me practice:

* Designing applications using Object-Oriented Programming
* Implementing encapsulation with private attributes
* Creating reusable classes and methods
* Managing persistent data with JSON
* Recording transaction history
* Working with dates and times using `datetime`
* Implementing secure user authentication
* Validating user input and handling exceptions
* Building a complete menu-driven console application

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400
