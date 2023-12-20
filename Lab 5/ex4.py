class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}")

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id)
        self.salary = salary
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Position: Manager, Salary: ${self.salary}, Department: {self.department}")

    def manage_team(self):
        print(f"{self.name} is managing the {self.department} team.")

class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Position: Engineer, Salary: ${self.salary}, Programming Language: {self.programming_language}")

    def code(self):
        print(f"{self.name} is coding in {self.programming_language}.")

class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, territory):
        super().__init__(name, employee_id)
        self.salary = salary
        self.territory = territory

    def display_info(self):
        super().display_info()
        print(f"Position: Salesperson, Salary: ${self.salary}, Territory: {self.territory}")

    def make_sale(self):
        print(f"{self.name} made a sale in {self.territory}.")

manager = Manager("Arhip Razvan", "1", 5000, "Marketing")
manager.display_info()
manager.manage_team()

engineer = Engineer("Sasha", "2", 6000, "Spring")
engineer.display_info()
engineer.code()

salesperson = Salesperson("Vamanu Petru", "3", 2000, "Truseni")
salesperson.display_info()
salesperson.make_sale()
