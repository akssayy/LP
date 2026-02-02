class person:
    def __init__(self, name):
        self.name = name

class student(person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

s = student("Akshay", 90)

print(s.name)
print(s.marks)