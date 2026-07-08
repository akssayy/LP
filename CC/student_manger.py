marks = [60, 70, 80]

def add_bonus(marks, bonus):
    for mark in marks:
        updated_marks = mark + bonus
        print(updated_marks)
        
    return marks.append(updated_marks) 


print(marks)
add_bonus(marks, 5)


