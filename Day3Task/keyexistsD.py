#Write a program to check whether a key exists in a dictionary
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

key = "Bob"

if key in students:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")