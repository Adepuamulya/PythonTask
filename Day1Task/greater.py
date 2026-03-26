#Write a program to check if one number is greater than another
# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Checking which number is greater
if num1 > num2:
    print("First number is greater")
elif num1 < num2:
    print("Second number is greater")
else:
    print("Both numbers are equal")