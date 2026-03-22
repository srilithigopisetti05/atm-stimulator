from file_handler import load_data, save_data
from auth import find_account, verify_pin
from transactions import withdraw, deposit, change_pin
from utils import get_float_input
import getpass
from file_handler import load_data, save_data
from auth import find_account, verify_pin
from transactions import withdraw, deposit, change_pin
from utils import get_float_input
import getpass


def print_receipt(action, amount, balance):
    from datetime import datetime

    print("\n" + "-"*30)
    print("        🧾 RECEIPT")
    print("-"*30)
    print(f"Transaction : {action}")
    print(f"Amount      : ₹{amount}")
    print(f"Balance     : ₹{balance}")
    print(f"Time        : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("-"*30 + "\n")


def run_atm():
    while True:
        accounts = load_data()

        print("ATM SIMULATOR")
        print("="*35)
        print("1. 💸 Withdraw")
        print("2. 💰 Deposit")
        print("3. 👤 View Profile")
        print("4. 🔐 Change PIN")
        print("5. ❌ Exit")
        print("="*35)

        choice = input("Enter choice: ").strip()

        if choice not in ["1", "2", "3", "4", "5"]:
            print("⚠️ Invalid choice. Try again.")
            continue

        if choice == "5":
            print("👋 Exiting... Thank you!")
            break

        acc_id = input("Enter Account ID: ").strip()
        account = find_account(accounts, acc_id)

        if not account:
            print("❌ Account not found.")
            continue

        # PIN required for sensitive operations
        if choice in ["1", "3", "4"]:
            pin = getpass.getpass("Enter PIN: ")
            if not verify_pin(account, pin):
                print("❌ Incorrect PIN.")
                continue

        # WITHDRAW
        if choice == "1":
            amount = get_float_input("Enter withdrawal amount: ")
            if amount is None:
                continue

            if withdraw(account, amount):
                save_data(accounts)
                print("✅ Withdrawal successful.")
                print_receipt("Withdrawal", amount, account["BALANCE"])

        # DEPOSIT
        elif choice == "2":
            amount = get_float_input("Enter deposit amount: ")
            if amount is None:
                continue

            if deposit(account, amount):
                save_data(accounts)
                print("✅ Deposit successful.")
                print_receipt("Deposit", amount, account["BALANCE"])

        # PROFILE
        elif choice == "3":
            print("\n--- 👤 Account Profile ---")
            print(f"Name    : {account['NAME']}")
            print(f"Balance : ₹{account['BALANCE']}")
            print("--------------------------")

        # CHANGE PIN
        elif choice == "4":
            new_pin = input("Enter new PIN: ").strip()
            if change_pin(account, new_pin):
                save_data(accounts)
                print("✅ PIN changed successfully.")


if __name__ == "__main__":
    run_atm()
