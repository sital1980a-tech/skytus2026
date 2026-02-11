class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)


student1 = Student("Alice", [85, 90, 78, 92])

average = student1.calculate_average()

print("Student Name:", student1.name)
print("Marks:", student1.marks)
print("Average Marks:", average)
