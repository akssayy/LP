students = [
  {"name": "A", "marks": 80},
  {"name": "B", "marks": 45},
  {"name": "C", "marks": 60}

]

def passed_students(students):
    passed = []
    for n in students:
        if n["marks"] >= 60:
            passed.append(n["name"])
        
    return passed

print(passed_students(students))