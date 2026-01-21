"""student = {"name" : "Akshay",
           "age" :  23,
           "marks" : 88}
print(student["name"],student["marks"])

student["marks"] = 90
student["city"] = "pune"
print(student)

for k, v in student.items():
    print(k, ":", v)"""

users = [
    {"id":1, "name":"A"},
    {"id":2, "name":"B"},
    {"id":3, "name":"C"}
]

for user in users:
    print(user["name"])
   