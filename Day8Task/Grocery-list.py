#Grocery List Manager 
#A user wants to save grocery items in a file grocery.txt. Write a Python program that takes multiple items from the user and writes them into the file, with each item on a new line.
n = int(input("Enter number of grocery items: "))

file = open("grocery.txt", "w")

for i in range(n):
    item = input("Enter item: ")
    file.write(item + "\n")

file.close()

file = open("grocery.txt", "r")
print("Grocery List:")
print(file.read())
file.close()