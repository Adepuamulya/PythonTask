#Write a program to find the student with the highest marks from a dictionary
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

highest_student = max(students, key=students.get)

print("Student with highest marks:", highest_student)
print("Marks:", students[highest_student])