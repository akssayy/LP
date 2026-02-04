import os

users = []

if os.path.exists("bank.txt"):
    f = open("bank.txt", "r")

    for line in f:
        line = line.strip()
        data = line.split(",")

        name = data[0]
        balance = int(data[1])

        users.append([name, balance])

    f.close()

print(users)


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        
        else:
            self.balance += amount
            print("Deposited: ", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount") 

        elif amount <= self.balance:
            self.balance -= amount
            print("Withdrawn: ", amount)

        else:
            print("Not enough balnance ")

    def show_details(self):
        print(self.name, "balance", self.balance)



accounts = []
if os.path.exists("bank.txt"):
    f = open("bank.txt", "r")
    data = f.read().split(",")
    f.close()
    
    name = data[0]
    balance = int(data[1])

else:
    name = "Akshay"
    balance = 1000

acc = BankAccount(name, balance)
while True:
    print("\n1 Deposit")
    print("\n2 Withdraw")
    print("\n3 Show balance")
    print("\n4 exit")

    choice = input("choose: ")

    if choice == "1":
        amt = int(input("Enter amount: "))
        acc.deposit(amt)
    
    elif choice == "2":
        amt = int(input("Enter amount: "))
        acc.withdraw(amt)

    elif choice == "3":
        acc.show_details()

    elif choice == "4":
        f = open("bank.txt", "w")
        f.write(acc.name + "," + str(acc.balance))
        f.close()
        print("DAta saved")
        break

    else:
        print("invalid choice")
        




"""acc2 = BankAccount("Rahul", 500)
acc2.deposit(200)
accounts.append(acc1)
accounts.append(acc2)

for acc in accounts:
    acc.show_details()"""