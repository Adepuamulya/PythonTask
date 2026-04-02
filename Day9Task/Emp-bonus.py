#Employee Bonus Calculator (Decorators & OOP) 
#A company wants to apply a bonus calculation automatically before displaying the 
#salary. Create an Employee class and use a decorator that modifies the salary by adding a bonus before displaying it.
def bonus_decorator(func):
    def wrapper(self):
        bonus = 1000
        self.salary = self.salary + bonus
        func(self)
    return wrapper

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @bonus_decorator
    def display_salary(self):
        print("Employee Name:", self.name)
        print("Salary with Bonus:", self.salary)

emp = Employee("Amulya", 20000)
emp.display_salary()