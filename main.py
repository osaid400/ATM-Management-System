# ==========================================
# ATM MANAGEMENT SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python 3.13
# =========================================== 

from src.manager import ATMManager
from src.ui import start_app

if __name__ == "__main__":
    manager = ATMManager()
    start_app(manager)