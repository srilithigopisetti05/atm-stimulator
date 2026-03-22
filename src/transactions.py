def withdraw(account, amount):
    balance = float(account["BALANCE"])

    if amount <= 0:
        print("Invalid amount.")
        return False

    if amount > balance:
        print("Insufficient balance.")
        return False

    balance -= amount
    account["BALANCE"] = f"{balance:.2f}"
    return True


def deposit(account, amount):
    if amount <= 0:
        print("Invalid amount.")
        return False

    balance = float(account["BALANCE"])
    balance += amount
    account["BALANCE"] = f"{balance:.2f}"
    return True


def change_pin(account, new_pin):
    if len(new_pin) != 4 or not new_pin.isdigit():
        print("Invalid PIN format.")
        return False

    account["PIN"] = new_pin
    return True