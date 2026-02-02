class Bank:
    def __init__(self):
        self.__balance = 1000 #private

    def show_balance(self):
        print(self.__balance)

b = Bank()
b.__balance = 9999
print(b.__balance)
print(b._Bank__balance)
b.show_balance()