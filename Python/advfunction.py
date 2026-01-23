"""numbers = [2, 4, 5, 7]

def add_numbers(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

result = add_numbers(numbers)
print(result)"""

numbers = [2, 5, 7, 4, 9]

def find_max(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i

    return max

result = find_max(numbers)
print(result)
