"""numbers = [1, 2, 3, 4, 5]

def sum_list(numbers):
    total = 0
    for i in numbers:
        total += i

    return  total

print(sum_list(numbers)"""


students = [
    {"name": "A", "marks": 55},
    {"name": "B", "marks": 70},
    {"name": "C", "marks": 60},
    {"name": "D", "marks": 30}
]


def check_passed(students):
    count = []
    for student in students:
        if student["marks"] >= 60:
            count.append(student["name"])

    return count

print(check_passed(students))