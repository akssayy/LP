
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
            try:
                amt = int(input("Enter amount to deposit: "))
                if amt <= 0:
                    print("Amount must be positive")

                else:
                    current.deposit(amt)
                    print("Deposited", amt)
            except ValueError:
                print("invalid Amouunt")
        elif choice == "2":
            try:
                 amt = int(input("Enter amount to withdraw: "))
                 if amt <= 0:
                    print("Amount must be positive")
                 else:  
                    current.withdraw(amt)
                    print("Withdrew", amt)

            except ValueError:
                print("Enter numbers only")

        elif choice == "3":
            current.show_details()

        elif choice == "4":
            
            print("Data saved!")
            break

        else:
            print("Invalid option. Please try again.")
    
