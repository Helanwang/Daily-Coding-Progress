def student(firstname, lastname="Mark"):

    print(f"Hello, {firstname} {lastname}!")


student("John")
student("John", "Doe")


class Person:
    def __init__(self, firstname="Helen", lastname="wang", age=30):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def display(self):
        print(f"Hello, {self.firstname} {self.lastname}")


person1 = Person()
person1.display()

person2 = Person("alice")
person2.display()

person3 = Person("Malcom", "Ben")
person3.display()


class HistoricalTemps:  # class example
    def __init__(self, zip_code: str, start: str = "1950-08-13", end: str = "2023-08-25"):
        self.zip_code = zip_code
        self.start = start
        self.end = end

    def display(self):
        print(f"Zip code: {self.zip_code}")
        print(f"Start date: {self.start}")
        print(f"End date: {self.end}")


historical_temps1 = HistoricalTemps("12345")
historical_temps1.display()

historical_temps2 = HistoricalTemps("12345", "11-21", "01-02")
historical_temps2.display()


class Item:
    def __init__(self, name: str, quantity: int = 5, price: int = 13):
        self.name = name
        self.quantity = quantity
        self.price = price

    def display(self):
        print(f"Name: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: {self.price}")


item1 = Item("Helen")
item1.display()


item2 = Item("Bob", quantity=5, price=100)
item2.display()
