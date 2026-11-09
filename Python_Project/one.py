FILENAME = "atm.txt"
import os

# Get the exact folder where this Python script is saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Force Python to look for atm.txt right inside that same folder
FILENAME = os.path.join(BASE_DIR, "atm.txt")

def read_data():
  
  with open(FILENAME, "r") as f:
    lines = [line.strip() for line in f.readlines()]

  if len(lines) < 2:
    return "1234", 10000.0, []

  stored_pin = lines[0]
  try:
    balance = float(lines[1])
  except ValueError:
    balance = 10000.0

  transactions = lines[2:] 
  return stored_pin, balance, transactions


def write_data(pin, balance, transactions):
  
  with open(FILENAME, "w") as f:
    f.write(f"{pin}\n")
    f.write(f"{balance}\n")
    for tx in transactions:
      f.write(f"{tx}\n")


def check_balance(balance):
  print(f"Current Balance: {int(balance)}")


def deposit(pin, balance, transactions):
  try:
    amount_str = input("Amount: ")
    amount = float(amount_str)
    if amount <= 0:
      print("Invalid amount. Please enter a value greater than zero.")
      return balance

    balance += amount
    
    tx = f"Deposit {int(amount)} | Balance: {int(balance)}"
    transactions.append(tx)
    write_data(pin, balance, transactions)
    print(f"Deposit successful. New Balance: {int(balance)}")
  except ValueError:
    print("Invalid amount. Please enter numbers only.")
  except Exception as e:
    print(f"An error occurred: {e}")
  return balance


def withdraw(pin, balance, transactions):
  try:
    amount_str = input("Amount: ")
    amount = float(amount_str)
    if amount <= 0:
      print("Invalid amount. Please enter a value greater than zero.")
      return balance
    if amount > balance:
      print("Insufficient balance.")
      return balance

    balance -= amount
    tx = f"Withdraw {int(amount)} | Balance: {int(balance)}"
    transactions.append(tx)
    write_data(pin, balance, transactions)
    print(f"Withdrawal successful. New Balance: {int(balance)}")
  except ValueError:
    print("Invalid amount. Please enter numbers only.")
  except Exception as e:
    print(f"An error occurred: {e}")
  return balance


def mini_statement(transactions):
  if not transactions:
    print("No recent transactions.")
  else:
    for i, tx in enumerate(transactions, 1):
      print(f"{i}. {tx}")


def main():
  stored_pin, balance, transactions = read_data()
  
  attempts = 3
  login_successful = False
  while attempts > 0:
    pin_input = input("PIN: ")
    if pin_input == stored_pin:
      print("Login successful")
      login_successful = True
      break
    else:
      attempts -= 1
      if attempts > 0:
        print(f"Invalid PIN. Attempts left: {attempts}")
      if attempts == 0:
        print("Account locked. Exiting...")

  if not login_successful:
    return


  while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Mini Statement")
    print("5. Exit")
    stored_pin, balance, transactions = read_data()
    try:
      choice = int(input("Menu option: "))
      if choice == 1:
        check_balance(balance)
      elif choice == 2:
        balance = deposit(stored_pin, balance, transactions)
      elif choice == 3:
        balance = withdraw(stored_pin, balance, transactions)
      elif choice == 4:
        mini_statement(transactions)
      elif choice == 5:
        print("Exiting... Thank you!")
        break
      else:
        print("Invalid menu option. Please choose between 1 and 5.")
    except ValueError:
      print("Invalid input. Please enter numbers only.")
      
if __name__ == "__main__":
  main()