import json

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

    def show_details(self):
        print(self.name, "balance:", self.balance)


# ---------- LOAD DATA ----------
try:
    f = open("data.json", "r")
    data = json.load(f)
    f.close()
except:
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

    if choice == "1":
        try:
            amt = int(input("Amount: "))
            if amt > 0:
                current.deposit(amt)
                print("Deposited", amt)
        except ValueError:
            print("Numbers only")

    elif choice == "2":
        try:
            amt = int(input("Amount: "))
            if amt > 0:
                current.withdraw(amt)
                print("Withdrew", amt)
        except ValueError:
            print("Numbers only")

    elif choice == "3":
        current.show_details()

    elif choice == "4":
        # SAVE TO JSON
        data[name] = current.balance

        f = open("data.json", "w")
        json.dump(data, f)
        f.close()

        print("Saved!")
        break

    else:
        print("Invalid choice")
