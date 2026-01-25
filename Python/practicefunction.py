numbers = [10, 25, 30, 45]

search = int(input("enter a number to search: "))

found = False

for number in numbers:
    if search == number:
        print("found:", number)
        found = True
        break

if not found:
    print("Not found")
    