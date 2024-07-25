# Multiple classes can be called using same method names
# Three classes: Car, Boat and Plane
# only one function : move()

class Car:
    def __init__(self, brand, model):  # Attributes
        self.brand = brand
        self.model = model

    def move(self):  # One method move()
        print("Drive!")


class Boat:
    def __init__(self, brand, model):  # Attributes
        self.brand = brand
        self.model = model

    def move(self):  # One method move()
        print("Sail!")


class Plane:
    def __init__(self, brand, model):  # Attributes
        self.brand = brand
        self.model = model

    def move(self):  # One method move()
        print("Fly!")


"""objects"""
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")


for x in (car1, boat1, plane1):
    x.move()  # calling the move method


"""
Drive!
Sail!
Fly!
"""