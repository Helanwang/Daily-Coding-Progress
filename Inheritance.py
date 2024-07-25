class Person:  # Class
    def __init__(self, first_name, last_name):  # Attributes
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):  # Methods
        print(self.first_name, self.last_name)


person1 = Person("Helen", "Wang")  # Objects
person1.print_name()  # Objects.Methods


class PersonChild(Person):  # Use the pass keyword when no any other properties or methods added to the class.
    pass


person_child = PersonChild("Jack", "Wang")
person_child.print_name()

