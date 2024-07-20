class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades


student1 = Student("Alice", "S123456", "[85, 92, 78]")

print(f"Student {student1.name} has grades {student1.grades}, ID is {student1.student_id}.")
