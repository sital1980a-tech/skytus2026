class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def display_salary_details(self):
        hra = 0.20 * self.basic_salary   
        da = 0.10 * self.basic_salary    
        gross_salary = self.basic_salary + hra + da

        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA (20%):", hra)
        print("DA (10%):", da)
        print("Gross Salary:", gross_salary)

emp1 = Employee(101, "John", 30000)
emp1.display_salary_details()
