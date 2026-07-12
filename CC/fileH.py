expenses = {}

try:
    with open("expenses.txt", "r") as file:
        data = file.readline()
except FileNotFoundError:
    return expenses
print(data)
