# Employee Management System (OOP + File + Dict) 
'''Scenario: 
Manage employee data. 
Task: 
● Create a class Employee 
● Store employees in a dictionary 
● Save data to a file 
● Use exception handling for invalid salary input 
● Use loop to display all employees'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
emps = {}
for i in range(2):
    name = input("Name: ")
    try:
        salary = int(input("Salary: "))
        emps[name] = salary
    except:
        print("Invalid input")
f = open("emp.txt", "w")
for name in emps:
    f.write(name + " " + str(emps[name]) + "\n")
f.close()
for name in emps:
    print(name, emps[name])