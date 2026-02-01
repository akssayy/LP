class vechical:
    def __init__(self, color, model, speed):
        self.color = color
        self.model = model
        self.speed = speed

    def show_type(self):
        print(self.color, self.model, self.speed)  
    
    def show_speed(self):
        self.speed = 120
        print(self.speed)

class car(vechical):
    def drive(self):
        print("car is running")
car1 = car("red", "mustang", 120)
car1.show_type()
car1.show_speed()
car1.drive()
car1.color("red")
