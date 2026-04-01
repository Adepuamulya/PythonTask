#Write a program to assign grades based on marks (for example: A, B, C, Fail). 
marks = float(input("Enter your marks (0-100): "))
if marks >= 90 and marks <= 100:
    grade = 'A'
elif marks >= 75:
    grade = 'B'
elif marks >= 50:
    grade = 'C'
elif marks >= 0:
    grade = 'Fail'
else:
    grade = 'Invalid marks'
print(f"Your grade is: {grade}")
