#Write a Python program using the math module to calculate and display the square 
#root, floor value, and ceiling value of a number entered by the user
import math

num = float(input("Enter a number: "))

sqrt_value = math.sqrt(num)
floor_value = math.floor(num)
ceil_value = math.ceil(num)

print("Square root:", sqrt_value)
print("Floor value:", floor_value)
print("Ceiling value:", ceil_value)