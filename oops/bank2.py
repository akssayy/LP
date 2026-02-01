class bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdraw sucessfully")
        else:
            print("Not enough money")

    def show_details(self):
        print(self.name, "balance: ", self.balance)
    
acc1 = bank("Akshay", 2000)
acc2 = bank("Rahul", 300)

acc2.deposit(100)
acc2.withdraw(50)
acc1.show_details()
acc2.show_details()