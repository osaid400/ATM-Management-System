import sys

def print_mini_statement(account, limit=5):
    transactions = list(reversed(account._transactions))[:limit]
    print("\n" + "=" * 60)
    print(f"Mini Statement for {account.name} ({account.account_number})".center(60))
    print("=" * 60)
    print(f"Current Balance: Rs. {account.balance:,.2f}")
    print("-" * 60)
    if not transactions:
        print("No transactions recorded yet.")
    else:
        for tx in transactions:
            tx_type = tx.get("Type", "Unknown")
            amount = tx.get("Amount", 0.0)
            date = tx.get("Date", "----/--/--")
            time = tx.get("Time", "--:--:--")
            print(f"{date} {time} | {tx_type:<22} | Rs. {amount:>10,.2f}")
    print("=" * 60)

def print_cash_statement(account, days=30):
    statement = account.statement(days=days)
    print("\n" + "=" * 60)
    print(f"{days}-Day Account Statement for {account.name}".center(60))
    print("=" * 60)
    print(f"Current Balance: Rs. {account.balance:,.2f}")
    print("-" * 60)

    if not statement:
        print(f"No transactions found in the last {days} days.")
        print("=" * 60)
        return

    header = f"{'Date':<12} {'Time':<10} {'Type':<22} {'Amount':>14}"
    print(header)
    print("-" * 60)

    for tx in statement:
        tx_type = tx.get("Type", "Unknown")
        amount = tx.get("Amount", 0.0)
        date = tx.get("Date", "----/--/--")
        time = tx.get("Time", "--:--:--")
        print(f"{date:<12} {time:<10} {tx_type:<22} Rs. {amount:>10,.2f}")

    print("=" * 60)

def run_fast_cash_menu(manager, account):
    print("\n" + "=" * 60)
    print("FAST CASH WITHDRAWAL".center(60))
    print("=" * 60)
    print("1. Rs. 1,000")
    print("2. Rs. 2,000")
    print("3. Rs. 5,000")
    print("4. Rs. 10,000")
    print("0. Back")
    print("-" * 60)

    fast_options = {"1": 1000, "2": 2000, "3": 5000, "4": 10000}
    choice = input("Select Fast Cash Option: ").strip()

    if choice in fast_options:
        amt = fast_options[choice]
        try:
            breakdown = manager.dispense_cash(account, amt)
            r_path = manager.generate_receipt(account, "Cash Withdrawal", amt, "ATM Fast Cash")
            print("\n" + "*" * 40)
            print(f" CASH DISPENSED: Rs. {amt:,.2f}".center(40))
            print(" Denominations:".center(40))
            print(f"   Rs. 1,000 x {breakdown['1000']}")
            print(f"   Rs.   500 x {breakdown['500']}")
            print("*" * 40)
            print(f"Remaining Balance: Rs. {account.balance:,.2f}")
            print(f"Receipt saved at: {r_path}")
        except ValueError as e:
            print(f"Transaction Failed: {e}")

def run_customer_menu(manager, account):
    while True:
        print("\n" + "=" * 60)
        print(f"Welcome, {account.name}".center(60))
        print("=" * 60)
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal (Other Amount)")
        print("3. Fast Cash")
        print("4. Fund Transfer (IBFT)")
        print("5. Change PIN")
        print("6. Mini Statement")
        print("7. 30-Day Statement")
        print("0. Exit / Logout")
        print("-" * 60)

        choice = input("Select Option: ").strip()

        if choice == "1":
            print(f"\nYour Current Balance: Rs. {account.balance:,.2f}")

        elif choice == "2":
            try:
                amt = float(input("Enter Amount to Withdraw (Multiples of 500): "))
                breakdown = manager.dispense_cash(account, amt)
                r_path = manager.generate_receipt(account, "Cash Withdrawal", amt, "ATM Withdrawal")
                print("\n" + "*" * 40)
                print(f" CASH DISPENSED: Rs. {amt:,.2f}".center(40))
                print(" Denominations:".center(40))
                print(f"   Rs. 1,000 x {breakdown['1000']}")
                print(f"   Rs.   500 x {breakdown['500']}")
                print("*" * 40)
                print(f"Remaining Balance: Rs. {account.balance:,.2f}")
                print(f"Receipt saved at: {r_path}")
            except ValueError as e:
                print(f"Transaction Failed: {e}")

        elif choice == "3":
            run_fast_cash_menu(manager, account)

        elif choice == "4":
            try:
                rec_num = input("Enter Recipient Account Number: ").strip()
                rec_acc = manager.find_account(rec_num)
                if not rec_acc:
                    print("Recipient Account Not Found.")
                    continue
                amt = float(input("Enter Transfer Amount: "))
                manager.transfer_money(account, rec_acc, amt)
                manager.generate_receipt(account, "Transfer Sent", amt, f"To {rec_acc.name}", "sent")
                manager.generate_receipt(rec_acc, "Transfer Received", amt, f"From {account.name}", "received")
                print(f"Transfer Successful! Remaining Balance: Rs. {account.balance:,.2f}")
            except ValueError as e:
                print(f"Transfer Failed: {e}")

        elif choice == "5":
            old_pin = input("Enter Current PIN: ").strip()
            new_pin = input("Enter New 4-Digit PIN: ").strip()
            try:
                account.change_pin(old_pin, new_pin)
                manager.save_accounts()
                print("PIN Changed Successfully!")
            except ValueError as e:
                manager.save_accounts()
                print(f"Action Failed: {e}")

        elif choice == "6":
            print_mini_statement(account, limit=5)

        elif choice == "7":
            print_cash_statement(account, days=30)

        elif choice == "0":
            print("Session Ended. Please collect your card.")
            break
        else:
            print("Invalid Choice!")

def run_admin_menu(manager):
    while True:
        print("\n" + "=" * 60)
        print("ATM MAINTENANCE & TECHNICIAN PANEL".center(60))
        print("=" * 60)
        print("1. View ATM Vault Balance")
        print("2. Refill ATM Cash Vault")
        print("3. View All Accounts")
        print("4. Unfreeze Account")
        print("0. Logout")
        print("-" * 60)

        choice = input("Select Option: ").strip()

        if choice == "1":
            print(f"\nCurrent ATM Vault Cash Balance: Rs. {manager.vault_balance:,.2f}")

        elif choice == "2":
            try:
                amt = float(input("Enter Cash Amount to Refill: "))
                manager.refill_vault(amt)
                print(f"Refill Successful! New Vault Balance: Rs. {manager.vault_balance:,.2f}")
            except ValueError as e:
                print(f"Refill Failed: {e}")

        elif choice == "3":
            print("\n" + "-" * 60)
            print(f"{'Acc No':<10} {'Holder Name':<15} {'Balance':<15} {'Status':<10}")
            print("-" * 60)
            for acc in manager.accounts:
                status = "ACTIVE" if acc.is_active else "FROZEN"
                print(f"{acc.account_number:<10} {acc.name:<15} Rs. {acc.balance:<12,.2f} {status:<10}")
            print("-" * 60)

        elif choice == "4":
            acc_num = input("Enter Account Number to Unfreeze: ").strip()
            acc = manager.find_account(acc_num)
            if acc:
                if acc.is_active:
                    print("Account is already Active.")
                else:
                    manager.unfreeze_account(acc)
                    print(f"Account {acc.account_number} ({acc.name}) Unfrozen Successfully!")
            else:
                print("Account Not Found.")

        elif choice == "0":
            print("Admin Logged Out.")
            break
        else:
            print("Invalid Choice!")

def start_app(manager):
    while True:
        print("\n" + "=" * 60)
        print("ATM AUTOMATED TELLER MACHINE".center(60))
        print("=" * 60)
        print("1. Customer Login (Insert Card)")
        print("2. Technician / Admin Panel")
        print("0. Exit Application")
        print("-" * 60)

        choice = input("Select Option: ").strip()

        if choice == "1":
            try:
                acc_num = input("Enter Account Number: ").strip()
                pin = input("Enter 4-Digit PIN: ").strip()
                acc = manager.find_account(acc_num)
                if acc:
                    try:
                        if acc.verify_pin(pin):
                            manager.save_accounts()
                            print("Authentication Successful!")
                            run_customer_menu(manager, acc)
                    except ValueError as e:
                        manager.save_accounts()
                        print(f"Authentication Failed: {e}")
                else:
                    print("Invalid Account Number.")
            except ValueError:
                print("Invalid input format.")

        elif choice == "2":
            user = input("Enter Admin Username: ").strip()
            password = input("Enter Admin Password: ").strip()
            if manager.admin_login(user, password):
                print("Admin Login Successful!")
                run_admin_menu(manager)
            else:
                print("Invalid Admin Credentials.")

        elif choice == "0":
            print("ATM Shutting Down. Goodbye!")
            sys.exit()
        else:
            print("Invalid Choice!")