class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


class Teacher(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")

if __name__ == "__main__":
    person = Person("John Doe", 25)
    student = Student("Alice Smith", 20, "S12345")
    teacher = Teacher("Mr. Johnson", 35, "T6789")

    person.display_info()
    print()
    student.display_info()
    print()
    teacher.display_info()

