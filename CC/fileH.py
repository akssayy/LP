def load_expenses():
    # Create an empty dictionary called expenses
    expenses = {}
    
    try:
        # Try to open expenses.txt in read mode
        with open("expenses.txt", "r") as file:
            # Read all lines from the file
            for line in file:
                clean_line = line.strip()  # Remove the newline character
                
                if not clean_line:  # Skip empty lines to prevent splitting errors
                    continue
                
                # Split the line by the comma, get category and amount
                category, amount = clean_line.split(",")
                
                # Convert amount to an integer and store it in the dictionary
                expenses[category.strip()] = int(amount.strip())
                
    except FileNotFoundError:
        # If the file doesn't exist, do nothing special
        pass
        
    # Return the dictionary
    return expenses

# Test it by printing the returned dictionary
print(load_expenses())
