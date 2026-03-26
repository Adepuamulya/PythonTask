#Write a program to check if a person is eligible to vote (age ≥ 18)
# Ask the user to enter their age
age = int(input("Enter your age: "))

# Check voting eligibility
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")