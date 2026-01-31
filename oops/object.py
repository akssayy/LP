class car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    
    def change_color(self, new_color):
        self.color = new_color

car1 = car(input("enter color: "), input("enter your car model: "))
car2 = car("black", "Audi")

car2.change_color("blue")

print(car1.color)
print(car2.color)