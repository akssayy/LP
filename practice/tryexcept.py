try: 
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:",result)

except ValueError:
    print("you must enter a number!")

except ZeroDivisionError:
    print("Number can't br zero!")

except Exception as e:
    print("Unexcepted error:", e) 




















"""try:
    num1 = int(input("enter a number: "))
    num2 = int(input("enter second number: "))

    result = num1 / num2
    print(f"{result}")
except ValueError:
    print("enter valid number")

except ZeroDivisionError:
    print("number can't be zero(0)")
"""


"""try:
    num = int(input("Enter a number to divide by 100: "))
    divide = 100 / num
    print(f"{divide}")
except ValueError:
    print("please enter a number")

except ZeroDivisionError:
    print("Cannot divide by zero")"""