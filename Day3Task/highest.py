#Write a program to find the student with the highest marks from a dictionary
students = {
    "Ammu": 85,
    "Nani": 90,
    "Chintu": 78
}

highest_student = max(students, key=students.get)

print("Student with highest marks:", highest_student)
print("Marks:", students[highest_student])
