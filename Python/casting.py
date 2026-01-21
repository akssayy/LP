# Type casting in Python is the process of converting a variable from one data type to another data type.
# Str() - Converts a value to a string data type.
# int() - converts a value to an integer data type.
# float() - converts a value to a float data type.
# bool() - converts a value to a boolean data type.

name = "akshay"
age = 21
gpa = 8.5
is_student = True

name = bool(name)
print(type(name))

age = str(age)
print(type(age))
print(age)

is_student = str(is_student)
print(type(is_student))
print(is_student)