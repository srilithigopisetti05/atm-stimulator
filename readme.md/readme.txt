# 🏦 ATM Transaction Simulator (Python CLI)

A modular, command-line based ATM simulation system built using Python.
This project replicates real-world ATM functionalities with persistent data storage and clean architecture.

---

## 🚀 Overview

The ATM Transaction Simulator allows users to perform essential banking operations such as withdrawals, deposits, PIN changes, and profile viewing through a CLI interface.

The system uses a CSV file (`accounts.csv`) for persistent storage, ensuring that all transactions are saved across program runs.

---

## ✨ Features

* 🔐 PIN-based authentication
* 💸 Cash withdrawal with balance validation
* 💰 Cash deposit with real-time updates
* 👤 View account profile
* 🔄 Change account PIN
* 🧾 Transaction receipt generation
* 📁 Persistent storage using CSV
* ⚠️ Input validation and error handling

---

## 🧠 Project Structure

```plaintext
atm-simulator/
│
├── data/
│   └── accounts.csv        # Stores account data
│
├── src/
│   ├── atm.py              # Main program (CLI + flow control)
│   ├── transactions.py     # Core transaction logic
│   ├── auth.py             # Authentication functions
│   ├── file_handler.py     # CSV read/write operations
│   └── utils.py            # Input validation helpers
│
├── README.md
└── .gitignore
```

---

## ⚙️ Technologies Used

* Python 3
* CSV Module (built-in)
* Command-Line Interface (CLI)

---

## ▶️ How to Run

1. Navigate to the project directory:

```bash
cd atm-stimulator/src
```

2. Run the program:

```bash
python atm.py
```

---

## 📊 Sample Data (`accounts.csv`)

```csv
ACC_ID,NAME,PIN,BALANCE
1001,Lithi,1234,5000.00
1002,Alex,5678,3000.00
```

---

## 🧾 Sample Output

```
------------------------------
        🧾 RECEIPT
------------------------------
Transaction : Deposit
Amount      : ₹500
Balance     : ₹5500.00
Time        : 23-03-2026 18:45:12
------------------------------
```

---

## 🧪 Testing

The system has been tested for:

* ✅ Data persistence across runs
* ✅ Invalid input handling
* ✅ Insufficient balance scenarios
* ✅ PIN validation
* ✅ File handling errors

---

## ⚠️ Limitations

* PIN is stored in plain text (not secure)
* CLI-based interface (no GUI)
* No transaction history logging

---

## 🔮 Future Enhancements

* 🔐 Encrypt PIN using `hashlib`
* 🧱 Convert to Object-Oriented Programming (OOP)
* 📝 Add transaction logging system
* 🗄️ Upgrade storage to SQLite
* 🌐 Build GUI or web interface

---

## 👤 Author

**Srilithi Gopisetti**

---

## ⭐ Final Note

This project demonstrates how core programming concepts—file handling, modular design, and validation—can be combined to simulate a real-world transactional system.

If you found this useful or interesting, consider giving it a ⭐ or building on top of it.
