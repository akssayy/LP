class car:
    def __init__(self, color, model, speed=0):
        self.color = color
        self.model = model 
        self.speed = speed
       
    
    def accelerate(self):
        self.speed += 10

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0


    def show_details(self):
        print("color:", self.color)
        print("model", self.model)
        print("speed", self.speed)
       

car1 = car("red", "Mustang")
car2 = car("White", "GT")

car1.accelerate()
car1.accelerate()
car2.accelerate()
print("------")
car1.show_details()
car2.show_details()

print("Applying brake....")
car1.brake()
car1.show_details()