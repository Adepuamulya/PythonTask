#Student Information System (Class & Object) 
#A school wants a program to store student details. Create a Student class with 
#attributes such as name, roll number, and marks. Create objects for at least three students and display their details.
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("Marks:", self.marks)
        print()

s1 = Student("Rahul", 1, 85)
s2 = Student("Anita", 2, 90)
s3 = Student("Ravi", 3, 78)

s1.display()
s2.display()
s3.display()