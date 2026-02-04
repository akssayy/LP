import os

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


# ---------- LOAD USERS ----------
users = []

if os.path.exists("bank.txt"):
    f = open("bank.txt", "r")

    for line in f:
        line = line.strip()
        data = line.split(",")

        name = data[0]
        balance = int(data[1])

        users.append(BankAccount(name, balance))

    f.close()

else:
    print("No bank file found")


# ---------- SHOW USERS ----------
print("\nLoaded Accounts:")
for acc in users:
    acc.show_details()
