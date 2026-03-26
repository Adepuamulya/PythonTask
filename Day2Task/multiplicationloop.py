#Write a program to print the multiplication table of a number using a loop.
# Ask the user to enter a number
num = int(input("Enter a number to print its multiplication table: "))

# Print the multiplication table using a for loop
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")