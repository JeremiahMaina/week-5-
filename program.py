class Vehicle:
    def move(self):
        pass 

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Bird(Vehicle):
    def move(self):
        print("Flying like a bird 🦅")

vehicles = [Car(), Plane(), Bird()]

for vehicle in vehicles:
    vehicle.move()