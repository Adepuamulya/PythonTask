#A company wants to organize its Python code using packages. 
#Create a package named utilities that contains two modules: 
# math_operations.py (functions for addition and multiplication) 
# string_operations.py (functions to convert string to uppercase and count characters) 
#Write a Python program that imports the package and uses functions from both modules.
from utilities import math_operations
from utilities import string_operations

print("Addition:", math_operations.add(10, 5))
print("Multiplication:", math_operations.multiply(10, 5))

text = "python programming"
print("Uppercase:", string_operations.to_uppercase(text))
print("Character Count:", string_operations.count_characters(text))