students = [
    {"name": "A", "marks": 55},
    {"name": "B", "marks": 70},
    {"name": "C", "marks": 40}
]

def check_result(students):
    passed = []
    
    for student in students:
        if student["marks"] >= 60:
            passed.append(student["name"])

    return passed

print(check_result(students))