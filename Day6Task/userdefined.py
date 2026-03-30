# Develop a Python program to manage student marks for three subjects. Store the subject 
#names in a tuple, maintain unique student names in a set, and store each student’s marks 
#in a list inside a dictionary where the key is the student name. Create user-defined 
#functions to add a student with marks, display all student records, and calculate the average 
#marks of a student. Implement a recursive function to calculate the total marks from the list of 
#marks. The program should interact with the user through a simple menu. Also include 
#exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError 
#(average calculation issues), TypeError (incorrect data type in marks), and NameError (when a 
#student name entered does not exist in the dictionary). 
#Example Output: 
#1. Add Student 
#2. Display Students 
#3. Calculate Average 
#4. Exit 
#Enter choice: 1 
#Enter student name: Rahul 
#Enter marks for Math: 80 
#Enter marks for Science: 85 
#Enter marks for English: 90 
#1. Add Student 
#2. Display Students 
#3. Calculate Average 
#4. Exit 
#Enter choice: 2 
#Rahul : [80, 85, 90] 
#1. Add Student 
#2. Display Students 
#3. Calculate Average 
#4. Exit 
#Enter choice: 3 
#Enter student name to calculate average: Rahul 
#Total Marks: 255 
#Average Marks: 85.0 
#1. Add Student 
#2. Display Students 
#3. Calculate Average 
#4. Exit 
#Enter choice: 4 
#Example of Exception Handling Output ValueError 
#Enter marks for Math: abc 
#Invalid input! Please enter numeric marks. NameError 
#Enter student name to calculate average: Ramesh Student name not found. ZeroDivisionError 
#Cannot divide by zero. TypeError 
#Marks data type error.
subjects = ("Math", "Science", "English")
students = set()
student_marks = {}

def recursive_total(marks, n):
    if n == 0:
        return 0
    return marks[n-1] + recursive_total(marks, n-1)

def add_student():
    try:
        name = input("Enter student name: ")
        marks = []
        for subject in subjects:
            m = int(input(f"Enter marks for {subject}: "))
            marks.append(m)
        students.add(name)
        student_marks[name] = marks
    except ValueError:
        print("Invalid input! Please enter numeric marks.")
    except TypeError:
        print("Marks data type error.")

def display_students():
    for name in student_marks:
        print(name, ":", student_marks[name])

def calculate_average():
    try:
        name = input("Enter student name to calculate average: ")
        if name not in student_marks:
            raise NameError
        marks = student_marks[name]
        total = recursive_total(marks, len(marks))
        print("Total Marks:", total)
        avg = total / len(marks)
        print("Average Marks:", avg)
    except NameError:
        print("Student name not found.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Marks data type error.")

while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        break
    else:
        print("Invalid choice")