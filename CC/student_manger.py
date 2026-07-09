expenses = {
    "Food": 6000,
    "Rent": 5500
}

def add_expense(category, amount):
        if category in expenses:
            expenses[category] += amount 
        else:
            expenses[category] = amount      
        
        return expenses 

def remove_expense(category):
    if category in expenses:
        expenses.pop(category)
    else:
        print("Category not found.")
    return expenses

def total_expense():
    return sum(expenses.values())

def highest_expense():
    i = 0
    for category, expense in expenses.items():
        if expense > i:
            i = expense
            highest_category = category
    
    return (highest_category, i)


def show_expenses():
    for index,category, expense in enumerate(expenses.items(), start=1):
        print(f"{index}.{category} {expense}")
    
    return expenses



result = add_expense("petrol", 1000)
print(result)

del_item = remove_expense("pocket money")
print(del_item)

total = total_expense()
print(total)

expensive = highest_expense()
print(expensive)
show_expenses()
