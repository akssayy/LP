f = open("numbers.txt", "w")
for number in range(5):
    numbers = int(input("enter a number: "))
    f.write(numbers )

f.close
f = open("numbers.txt", "r")
content = f.read()
print(content)

for i in content:
    total = 0
    total += i

print(total)    