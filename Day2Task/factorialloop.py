#Write a program to calculate the factorial of a number using a loop.
num = int(input("Enter a non-negative integer: "))
factorial = 1
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is: {factorial}")
