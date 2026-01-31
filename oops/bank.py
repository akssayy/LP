class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

        else:
            print("Insufficent balance")
        
    
    def show_details(self):
        print("Name", self.name)
        print("Balance: ", self.balance)

acc1 = BankAccount("Akshay")
acc1.deposit(500)
acc1.withdraw(200)
acc1.withdraw(400)

acc1.show_details()
