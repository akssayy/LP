age = int(input("enter your age: "))

def check_age(age):
    if age < 18:
        return "child"
    
    elif  age <=59:
        return "adult"
    
    else:
        return " senior"

a = check_age(age)
print(a)





"""
x = [5, 6]
y = x
y = y + [7]
print(x)
print(y)
"""
"""number = int(input("Enter a number: "))

def square(number):
    return number * number

s= square(number)
print(s)
"""