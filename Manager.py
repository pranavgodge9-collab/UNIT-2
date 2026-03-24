class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id

class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id)
        self.department = department

    def show_info(self):
        print(f"Manager: {self.name}, ID: {self.emp_id}, Dept: {self.department}")

m = Manager("John", 40, "M45", "IT")
m.show_info()
