numbers = [2, 4, 5, 7]

def add_numbers(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

result = add_numbers(numbers)
print(result)