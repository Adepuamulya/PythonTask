#Write a program to remove duplicate values from a list using a set
numbers = [10, 20, 10, 30, 20, 40, 50, 40]

unique_numbers = list(set(numbers))

print("List after removing duplicates:", unique_numbers)