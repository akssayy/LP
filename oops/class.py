class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Akshay", 23)
s2 = Student("Rahul", 22)

s1.show()
print("----")
s2.show()
