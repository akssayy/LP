import os
print(os.getcwd())
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

#-----------CHOOSE ACCOUNT ----------
name = input("\nEnter account name: ")

current = None
for acc in users:
    if acc.name == name:
        current = acc
        break

if current:

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Show Details")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amt = int(input("Enter amount to deposit: "))
            current.deposit(amt)
            print("Deposited", amt)

        elif choice == "2":
            amt = int(input("Enter amount to withdraw: "))
            current.withdraw(amt)
            print("Withdrew", amt)

        elif choice == "3":
            current.show_details()

        elif choice == "4":
            f = open("bank.txt", "w")

            for acc in users:
                line = acc.name + "," + str(acc.balance) + "\n"
                f.write(line)
            f.close()

            print("Data saved!")
            break

        else:
            print("Invalid option. Please try again.")
    
