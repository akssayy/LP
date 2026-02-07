try:
    num = int(input("Enter a number to divide by 100: "))
    divide = 100 / num
    print(f"{divide}")
except ValueError:
    print("please enter a number")

except ZeroDivisionError:
    print("Cannot divide by zero")