def load_expenses():
    expenses = {}
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                clean_line = line.strip()

                category, amount = clean_line.split(",")
                amount = int(amount)
                expenses[category] = int(amount)


    except FileNotFoundError:
        pass
    t = type(amount)
    print(t)
    return expenses

result = load_expenses()
print(result)
