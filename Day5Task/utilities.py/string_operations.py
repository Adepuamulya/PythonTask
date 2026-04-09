#A company wants to organize its Python code using packages. 
#Create a package named utilities that contains two modules: 
# math_operations.py (functions for addition and multiplication) 
# string_operations.py (functions to convert string to uppercase and count characters) 
#Write a Python program that imports the package and uses functions from both modules.
def to_uppercase(text):
    return text.upper()
def count_characters(text):
    return len(text)
