def find_account(accounts, acc_id):
    for acc in accounts:
        if acc["ACC_ID"] == acc_id:
            return acc
    return None

def verify_pin(account, pin):
    return account["PIN"] == pin