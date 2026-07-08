marks = [60, 70, 80]

def add_bonus(marks, bonus):
    new_list = []
    for mark in marks:
        updated_marks = mark + bonus
        new_list.append(updated_marks) 

    return new_list

print(marks)
print(add_bonus(marks, 5))
print(add_bonus(marks,10))



