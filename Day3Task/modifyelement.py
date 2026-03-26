#Write a program to convert a tuple to a list and modify the element.
my_tuple = (10, 20, 30, 40, 50)

my_list = list(my_tuple)

my_list[2] = 99

print("Modified list:", my_list)