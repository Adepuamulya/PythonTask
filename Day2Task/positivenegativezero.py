#Write a program to check whether a number is positive, negative, or zero
# Ask the user to enter a number
num = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print("The number is zero.")