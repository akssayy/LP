expenses = {}

try:
    with open("expenses.txt", "r") as file:
        data = file.readlines()
except FileNotFoundError:
    print(expenses)
print(data)
