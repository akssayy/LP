expenses = {}

try:
    with open("expenses.txt", "r") as file:
        for line in file:
            print(line.strip(), line.split(","))
except FileNotFoundError:
    print(expenses)
print(file)
