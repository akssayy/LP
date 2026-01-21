student = {"name" : "Akshay",
           "age" :  23,
           "marks" : 88}
print(student["name"],student["marks"])

student["marks"] = 90
student["city"] = "pune"
print(student)

for k, v in student.items():
    print(k, ":", v)