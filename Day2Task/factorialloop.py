#Write a program to calculate the factorial of a number using a loop.
# Ask the user to enter a number
num = int(input("Enter a non-negative integer: "))

# Initialize factorial to 1
factorial = 1

# Check for negative input
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate factorial using a for loop
    for i in range(1, num + 1):
        factorial *= i
    # Display the result
    print(f"The factorial of {num} is: {factorial}")