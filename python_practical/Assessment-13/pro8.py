class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Derived Class 1
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
    
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display_teacher_info(self):
        self.display_info()
        print(f"Subject: {self.subject}")
        print(f"Salary: {self.salary}")


# Derived Class 2
class Student(Person):
    def __init__(self, name, age, grade, marks):
    
        super().__init__(name, age)
        self.grade = grade
        self.marks = marks

    def display_student_info(self):
        self.display_info()
        print(f"Grade: {self.grade}")
        print(f"Marks: {self.marks}")


# -------- Testing --------

teacher1 = Teacher("Mr. Sharma", 40, "Mathematics", 50000)
student1 = Student("Rahul", 16, "10th", 88)

print("Teacher Details:")
teacher1.display_teacher_info()

print("\nStudent Details:")
student1.display_student_info()
