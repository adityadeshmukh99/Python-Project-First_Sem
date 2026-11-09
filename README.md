# ATM Management System

A Python 3 console-based ATM simulation project featuring user authentication, balance checking, deposits, withdrawals, mini statement tracking, robust error handling, and text file data persistence[cite: 1].

## Features
- **Secure PIN Authentication:** Verifies the user PIN with a maximum of 3 attempts before locking the account[cite: 1].
- **Core Operations:** Supports balance checking, money deposits, withdrawals, and mini statements using modular functions[cite: 1].
- **Data Persistence:** Automatically saves updated account balances and transaction histories to `atm.txt` after every operation[cite: 1].
- **Exception Handling:** Gracefully handles invalid numeric entries, text inputs, and file errors using `try-except` blocks[cite: 1].

## Default Credentials & Data (`atm.txt`)
The program reads from and writes to an adjacent `atm.txt` file structured as follows[cite: 1]:
- **Default PIN:** `1234`[cite: 1]
- **Opening Balance:** `10000`[cite: 1]

## How to Run

1. Make sure you have **Python 3** installed on your system.
2. Download or clone this repository ensuring both your python script (e.g., `one.py`) and `atm.txt` are placed **in the same folder**.
3. Open your terminal or command prompt inside that folder.
4. Run the program using the command:
   ```bash
   python one.py
