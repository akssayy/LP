try:
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
except ValueError:
    print("Please enter a number only")


user_choice = input("enter action you want to perform, +, -, *, / : ")

def calculator(num1, num2, user_choice):
    if user_choice == "+":
        return num1 + num2
    
    elif user_choice == "-":
        return num1 - num2
    
    elif user_choice == "*":
        return num1 * num2

    elif user_choice == "/":
        return num1 / num2

    else:
        print("invalid choice")

result = calculator(num1, num2, user_choice)
print(result)

