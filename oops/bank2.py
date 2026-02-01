class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Invaild amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdraw sucessfully")
        else:
            print("Not enough money")

    def transfer(self, other_account, amount):
        if amount <= 0:
            print("invalid amount")

        elif amount <= self.balance:
            self.balance -= amount
            other_account += amount
            print(f"{amount} transferred to {other_account} ")


    def show_details(self):
        print(self.name, "balance: ", self.balance)
    
acc1 = Bank("Akshay", 1000)
acc2 = Bank("Rahul", 500)
acc3 = Bank("Neha", 200)
acc2.transfer(acc1, 100)

#acc2.deposit(100)
#.withdraw(50)
acc1.show_details()
acc2.show_details()
acc3.show_details()