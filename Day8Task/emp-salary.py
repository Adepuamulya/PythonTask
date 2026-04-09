# Employee Salary Management System 
#A company stores employee data in a file employees.txt in the format: EmployeeName Salary 
#Example: 
#Ramesh 25000 
#Sita 30000 
#Arun 28000 
#Write a Python program that: 
#● Reads employee data from the file 
#● Displays all employee details 
#● Finds the employee with the highest salary 
#● Appends a new employee record to the file.
file = open("employees.txt", "r")
highest_salary = 0
highest_employee = ""
print("Employee Details:")
for line in file:
    name, salary = line.split()
    salary = int(salary)
    print(name, salary)

    if salary > highest_salary:
        highest_salary = salary
        highest_employee = name
file.close()
print("Employee with Highest Salary:", highest_employee, highest_salary)

name = input("Enter new employee name: ")
salary = input("Enter salary: ")

file = open("employees.txt", "a")
file.write(name + " " + salary + "\n")
file.close()
