"""
num = int(input("enter a number"))

if num > 0:
    print("positive")

elif num < 0 :
    print("negitive")
else:
    print("zero")

age = int(input("enter your age: "))

if age >= 18:
    print("eligible")

else:
    print("not eligible")
 """
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("num1 is bigger")
elif num2 >= num1 and num2 >= num3:
    print("num2 is bigger")
else:
    print("num3 is bigger")