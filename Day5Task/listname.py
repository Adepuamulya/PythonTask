#Write a program that uses random.choice() to randomly select a student from a 
#list and display: "The selected student for presentation is: <name>"
import random

students = ["Amulya", "Rohith", "Sita", "Ramu", "Priya"]

name = random.choice(students)

print("The selected student for presentation is:", name)