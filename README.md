
# ATM Management System 

A beginner-friendly console-based ATM Management System built using Python. This project demonstrates menu-driven programming, functions, JSON file handling, input validation, and exception handling while simulating basic ATM operations.

## Features

* Login using Account Number and PIN
* Check Account Balance
* Deposit Money
* Withdraw Money
* Change PIN
* Logout
* Store account data using JSON
* Input Validation
* Exception Handling

## Technologies Used

* Python 3
* JSON

## Project Structure

```text
ATM-Management-System/
│
├── ATM Management System.py
├── .gitignore
└── README.md
```

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/osaid400/ATM-Management-System.git
```

2. Navigate to the project folder.

```bash
cd ATM-Management-System
```

3. Run the program.

```bash
python "ATM Management System.py"
```

---

# Example Outputs

## Login

```text
============ Welcome to ATM Management System =============

=============== Select the Option ===============
1. Login
0. Exit

Enter the number: 1

Enter the Account number: 3012
Enter the pin: 3457

Login Successful
```

---

## Check Balance

```text
=============== Select the Option ===============
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Change Pin
5. Logout
0. Back to Main Menu

Enter the number: 1

Current Balance: Rs. 23,000
```

---

## Deposit Money

```text
Enter the number: 2

Enter Amount: 5000

Money Deposited Successfully!
```

---

## Withdraw Money

```text
Enter the number: 3

Enter Amount: 2000

Money Withdrawn Successfully!
```

---

## Change PIN

```text
Enter the number: 4

Enter current PIN: 3457
Enter new PIN: 9876

PIN changed successfully!
```

---

## Incorrect PIN

```text
Enter current PIN: 1111

Incorrect PIN!
```

---

## Insufficient Balance

```text
Enter Amount: 90000

Insufficient Balance!
```

---

## Logout

```text
Enter the number: 5

Logged out successfully.
```

---

## Invalid Login

```text
Enter the Account number: 3012
Enter the pin: 1234

Invalid Login
```

---

## Concepts Practiced

* Functions
* Lists & Dictionaries
* JSON File Handling
* Loading and Saving Data
* Conditional Statements
* Loops
* Input Validation
* Exception Handling
* Menu-Driven Programming

## Future Improvements

* Transaction History
* Money Transfer Between Accounts
* PIN Confirmation Before Transactions
* Account Lock After Multiple Wrong PIN Attempts
* SQLite Database Integration
* Object-Oriented Programming (OOP) Version

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400
