students = {
    "Akshay": 87,
    "virat": 75
}

def add_student(name, marks):
    
    if name in students:
        print("Student already exits.")

    else:
        students.update({name: marks})
        print(students)

def update_marks(name, marks):

    if name in students:
        students[name] = marks
        print(students)

    else:
        print("Student not found")

def calculate_average(students):
    x = len(students)
    return "Class Average: ",sum(students.values())/ x

def show_students():

    for index, student in enumerate(students, start=1):
        print(f"{index}. {student}")


add_student("ABD", 87)
update_marks("Akshay", 77)
show_students()
calculate_average(students)

