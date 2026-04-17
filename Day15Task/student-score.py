# Student Score Processor 
'''Scenario: 
A teacher stores student names and marks in a list of tuples. 
Task: 
● Convert data into a dictionary 
● Use a loop + condition to find students scoring above 50 
● Use math module to calculate average 
● Store results in a text file '''
import math
students = [("Ravi", 65), ("Sita", 45), ("Aman", 78), ("Neha", 50)]
student_dict = dict(students)
above_50 = {}
for name, marks in student_dict.items():
    if marks > 50:
     above_50[name] = marks
avg = sum(student_dict.values()) / len(student_dict)
avg = math.floor(avg)
file = open("result.txt", "w")
file.write(str(student_dict) + "\n")
file.write(str(above_50) + "\n")
file.write("Average: " + str(avg))
file.close()

print("Done")