import csv
import sys

FILE_PATH = "../data/accounts.csv"

def load_data():
    try:
        with open(FILE_PATH, mode='r') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print("Error: accounts.csv not found.")
        sys.exit()

def save_data(accounts):
    with open(FILE_PATH, mode='w', newline='') as file:
        fieldnames = ["ACC_ID", "NAME", "PIN", "BALANCE"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(accounts)