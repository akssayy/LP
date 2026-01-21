"""marks = (12, 45, 85, 65, 69)
#marks[1] = 22
y = list(marks)
print(type(y))
y.append(22)
marks = tuple(y)
print(marks)
print(type(marks))"""

tuple = (23, 34, 45, 56)
newt = (67,)
tuple += newt

print(tuple)