# Project Summary: ATM Management System (PS No. 99)

## Overview
* **Project Title:** ATM Management System
* **Language:** Python 3
* **Concepts Used:** Conditions, Loops, Functions, Exceptions, File Handling
* **Default Data:** Default PIN is `1234` and the opening balance is `10000` (stored in `atm.txt`). Each test case starts with this default data.

## Problem Statement
Create a menu-driven ATM simulation where a user logs in with a PIN and can check their balance, deposit funds, withdraw funds, and view a mini statement. Account data and transactions must be stored in a file.

## Bare Minimum Requirements
1. Write the solution in Python 3 (one `.py` file) and run it from the console.
2. Verify the PIN with a maximum of 3 attempts using a loop.
3. Implement balance check, deposit, withdraw, and mini statement features using functions.
4. Handle invalid inputs and file errors using `try-except` blocks.
5. Save the balance and transactions to a file after every operation.

## Test Cases
* **Test Case 1 (Normal Input):** Login with PIN `1234`, select Deposit (Option 2), deposit `5000` -> Expected output: Login successful, Deposit successful with new balance `15000`.
* **Test Case 2 (Boundary / Minimum Input):** Login with PIN `1234`, select Withdraw (Option 3), withdraw `10000` (equal to balance) -> Expected output: Withdrawal successful, New Balance: `0`.
* **Test Case 3 (Invalid Input):** Enter incorrect PINs (`1111`, then `2222`, then `3333`) -> Expected output: Invalid PIN attempts left, followed by "Account locked. Exiting...".
* **Test Case 4 (Different Valid Scenario):** Login with PIN `1234`, enter invalid withdrawal amount `abc`, then valid withdrawal `2000`, then view mini statement (Option 4) -> Expected output: Handles invalid amount error, completes valid withdrawal (New Balance: `8000`), and displays the mini statement.

## Instructions & Deliverables
1. Define and understand the problem statement.
2. Develop the solution using proper logic and programming concepts.
3. Implement all features and pass the test cases.
4. Test and debug the project for correct output.
5. Prepare documentation/report and upload code and report to GitHub.
6. Complete and submit the project within the deadline.
