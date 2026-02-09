import json

# ---------- SAVE FUNCTION ----------
def save_data():
    with open("data.json", "w") as f:
        json.dump(data, f)


# ---------- CLASS ----------
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Not enough balance!")
            return False

    def show_details(self):
        print(self.name, "balance:", self.balance)


# ---------- LOAD DATA ----------
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}

print("\nLoaded Accounts:")
for name, bal in data.items():
    print(name, "balance:", bal)

# ---------- CHOOSE ACCOUNT ----------
name = input("\nEnter account name: ")

if name not in data:
    print("New account created!")
    data[name] = 0

current = BankAccount(name, data[name])

# ---------- MENU ----------
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Details")
    print("4. Exit")

    choice = input("Choose: ")

    # ----- DEPOSIT -----
    if choice == "1":
        try:
            amt = int(input("Amount: "))
            if amt > 0:
                current.deposit(amt)
                data[name] = current.balance
                save_data()
                print("Deposited", amt)
            else:
                print("Enter positive amount!")
        except ValueError:
            print("Numbers only")

    # ----- WITHDRAW -----
    elif choice == "2":
        try:
            amt = int(input("Amount: "))
            if amt > 0:
                success = current.withdraw(amt)
                if success:
                    data[name] = current.balance
                    save_data()
                    print("Withdrew", amt)
            else:
                print("Enter positive amount!")
        except ValueError:
            print("Numbers only")

    # ----- SHOW -----
    elif choice == "3":
        current.show_details()

    # ----- EXIT -----
    elif choice == "4":
        data[name] = current.balance
        save_data()
        print("Saved! Goodbye.")
        break

    else:
        print("Invalid choice")
