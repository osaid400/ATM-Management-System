# ATM Management System

A console-based **ATM Management System** built with Python. This project simulates real-world Automated Teller Machine (ATM) operations while demonstrating Object-Oriented Programming (OOP), SHA-256 security hashing, multi-panel separation, cash vault management, JSON-based data persistence, transaction logging, input validation, modular design, and exception handling.

## Key Features

* **Dual Panel Architecture:** Distinct **Customer ATM Portal** and **Admin / Maintenance Panel**.
* **SHA-256 Security:** PINs are stored securely as SHA-256 hashes instead of plaintext.
* **3-Attempt Account Lockout:** Automatically freezes account after 3 consecutive invalid PIN attempts (Admin unfreeze required).
* **Withdrawal Denomination Breakdown:** Strictly enforces multiples of Rs. 500/1000 and calculates note breakdown (e.g., Rs. 3,500 = 3x Rs. 1,000 + 1x Rs. 500).
* **ATM Cash Vault Tracking:** Real-time machine vault balance tracking with "ATM Out of Cash" safeguards and Admin refill capabilities.
* **Daily Withdrawal Limit:** Enforces a maximum withdrawal limit of Rs. 50,000 per day.
* **Fast Cash Withdrawal:** One-click quick cash options (Rs. 1k, 2k, 5k, 10k).
* **Fund Transfer (IBFT):** Secure account-to-account money transfers.
* **Statements & Receipts:** Supports Mini Statements (Last 5 transactions), 30-Day Cash Statements, and automated `.txt` receipt generation inside structured subfolders (`receipts/`).
* **Persistent Storage:** JSON file persistence for accounts (`data/accounts.json`) and vault balance (`data/vault.json`).

## Technologies Used

* **Python 3**
* **JSON** (Data Persistence)
* **Hashlib** (SHA-256 Encryption)

## Concepts Covered

* Object-Oriented Programming (OOP)
* Encapsulation (`private attributes` & `@property`)
* Data Security & Hashing (`hashlib.sha256`)
* Modular Architecture & Package Structuring
* File Persistence & JSON Handling
* Date & Time Processing (`datetime` & `timedelta`)
* Exception Handling & Input Validation
* Menu-Driven CLI Design

## Project Structure

```text
ATM Management System/
│
├── data/
│   ├── accounts.json         # Persistent JSON account records
│   └── vault.json            # ATM Machine vault cash tracking
│
├── receipts/                 # Auto-generated transaction receipts
│   ├── general/              # Withdrawal & general receipts
│   ├── received/             # IBFT transfer received receipts
│   └── sent/                 # IBFT transfer sent receipts
│
├── src/                      # Source code modules
│   ├── __init__.py
│   ├── manager.py            # ATMManager business, security & persistence logic
│   ├── models.py             # BankAccount model & encapsulation logic
│   └── ui.py                 # Customer & Admin CLI menus
│
├── .gitignore                # Excludes pycache, receipts, and local data
├── main.py                   # Application entry point
└── README.md                 # Project documentation

```

## Sample Default Accounts

> **Note:** Default PIN for all sample accounts is `1234`. Upon first run/transaction, the PIN is automatically hashed into SHA-256.

| Account Holder | Account Number | Initial Balance | Initial Status |
| --- | --- | --- | --- |
| Ali | 3011 | Rs. 25,000.00 | Active |
| Abdullah | 3012 | Rs. 45,000.00 | Active |
| Ahmed | 3013 | Rs. 30,000.00 | Active |
| Zohaib | 3014 | Rs. 55,000.00 | Active |
| Fabiha | 3015 | Rs. 18,000.00 | Active |

**Admin / Technician Panel Credentials:**

* **Username:** `admin`
* **Password:** `12345`

## How to Run

1. Clone the repository:

```bash
git clone [https://github.com/osaid400/ATM-Management-System.git](https://github.com/osaid400/ATM-Management-System.git)

```

2. Navigate to the project folder:

```bash
cd ATM-Management-System

```

3. Run the application:

```bash
python main.py

```

## Example Outputs

### 1. Main Welcome Portal

```text
============================================================
                ATM AUTOMATED TELLER MACHINE                
============================================================
1. Customer Login (Insert Card)
2. Technician / Admin Panel
0. Exit Application
------------------------------------------------------------
Select Option: 1

```

### 2. Customer ATM Main Menu

```text
============================================================
                      Welcome, Abdullah                     
============================================================
1. Balance Inquiry
2. Cash Withdrawal (Other Amount)
3. Fast Cash
4. Fund Transfer (IBFT)
5. Change PIN
6. Mini Statement
7. 30-Day Statement
0. Exit / Logout
------------------------------------------------------------
Select Option: 

```

### 3. Cash Withdrawal & Denomination Breakdown

```text
Enter Amount to Withdraw (Multiples of 500): 3500

****************************************
          CASH DISPENSED: Rs. 3,500.00  
             Denominations:             
               Rs. 1,000 x 3
               Rs.   500 x 1
****************************************
Remaining Balance: Rs. 41,500.00
Receipt saved at: receipts/general/3012_TXN0001.txt

```

### 4. Fast Cash Menu

```text
============================================================
                    FAST CASH WITHDRAWAL                    
============================================================
1. Rs. 1,000
2. Rs. 2,000
3. Rs. 5,000
4. Rs. 10,000
0. Back
------------------------------------------------------------
Select Fast Cash Option: 3

****************************************
          CASH DISPENSED: Rs. 5,000.00  
             Denominations:             
               Rs. 1,000 x 5
               Rs.   500 x 0
****************************************
Remaining Balance: Rs. 36,500.00
Receipt saved at: receipts/general/3012_TXN0002.txt

```

### 5. Fund Transfer (IBFT)

```text
Enter Recipient Account Number: 3011
Enter Transfer Amount: 5000
Transfer Successful! Remaining Balance: Rs. 31,500.00

```

### 6. Mini Statement Display

```text
============================================================
             Mini Statement for Abdullah (3012)             
============================================================
Current Balance: Rs. 31,500.00
------------------------------------------------------------
2026-08-10 10:15:30 | Transfer Sent          | Rs.   5,000.00
2026-08-10 10:12:04 | Cash Withdrawal        | Rs.   5,000.00
2026-08-10 10:08:18 | Cash Withdrawal        | Rs.   3,500.00
============================================================

```

### 7. Account Freeze on 3 Failed PIN Attempts

```text
Enter Account Number: 3012
Enter 4-Digit PIN: 0000
Authentication Failed: Incorrect PIN! Remaining attempts: 2

Enter 4-Digit PIN: 0000
Authentication Failed: Incorrect PIN! Remaining attempts: 1

Enter 4-Digit PIN: 0000
Authentication Failed: Account FROZEN due to 3 consecutive wrong PIN attempts! Contact Admin.

```

### 8. Admin / Maintenance Panel & Unfreezing

```text
============================================================
             ATM MAINTENANCE & TECHNICIAN PANEL             
============================================================
1. View ATM Vault Balance
2. Refill ATM Cash Vault
3. View All Accounts
4. Unfreeze Account
0. Logout
------------------------------------------------------------
Select Option: 4

Enter Account Number to Unfreeze: 3012
Account 3012 (Abdullah) Unfrozen Successfully!

```

## Future Improvements

* SQLite or PostgreSQL database integration replacing JSON persistence
* RESTful API backend implementation (using FastAPI / Flask)
* Graphical User Interface (GUI using PyQt or CustomTkinter)
* OTP / Two-Factor Authentication simulation for high-value transactions

## Author

**MUHAMMAD ABDULLAH FAROOQ**

GitHub: https://github.com/osaid400

