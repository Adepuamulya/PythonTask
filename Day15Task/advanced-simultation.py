# Advanced Simulation System 
'''Scenario: 
Simulate exam results and generate reports. 
Task: 
● Generate random marks using random 
● Store in NumPy array 
● Convert to Pandas DataFrame 
● Use OOP to represent Student 
● Use conditions + loops to assign grades 
● Save report to file 
● Handle errors using try-except 
● Use math module for statistics'''
import random
import numpy as np
import pandas as pd
import math
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
names = ["Rohith", "Amulya", "Nani"]
try:
    marks = np.array([random.randint(30, 100) for i in range(len(names))])
    grades = []
    for m in marks:
        if m >= 75:
            grades.append("A")
        elif m >= 50:
            grades.append("B")
        else:
            grades.append("C")
    df = pd.DataFrame({
        "Name": names,
        "Marks": marks,
        "Grade": grades
    })
    print(df)
    avg = math.floor(sum(marks) / len(marks))
    print("Average:", avg)
    f = open("report.txt", "w")
    f.write(df.to_string())
    f.close()
except:
    print("Error")