students = []

def add_student(name):
    students.append(name)

add_student("Akshay")
add_student("vijay")
print(students)

def remove_student(name):
    if name in students:
         students.remove(name)
    else:
        print("student not found")

remove_student("Akshay")
print(students)

def show_student():
    
    for index, student in enumerate(students, start=1):
        print(index, student)
        
    
    print(f"no of students are{i}")

show_student()