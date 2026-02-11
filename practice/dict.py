"""numbers = [1, 2, 3, 4, 5]

def sum_list(numbers):
    total = 0
    for i in numbers:
        total += i

    return  total

print(sum_list(numbers)"""


numbers = [1, 2, 3, 4, 5, 6]


def check_passed(students):
    result = {
        "even": [],
        "odd": []
    }

    for n in numbers:
        if n %2 == 0:
            result ["even"].append(n)
        else:
            result ["odd"].append(n)

    return result

print(check_passed(numbers))