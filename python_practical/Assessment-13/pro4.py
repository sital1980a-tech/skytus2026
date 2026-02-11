class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Position: {self.position}")

class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.department = department

    def display_manager_info(self):
        self.display_person_info()
        self.display_employee_info()
        print(f"Department: {self.department}")

manager = Manager("Alice", 35, "E123", "Team Lead", "IT")

manager.display_manager_info()
