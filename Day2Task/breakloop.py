#Write a program that searches for a number in a list and breaks the loop when found.
# Define a list of numbers
numbers = [4, 7, 1, 9, 12, 5]

# Ask the user for the number to search
target = int(input("Enter the number to search: "))

# Search for the number
for num in numbers:
    if num == target:
        print(f"{target} found in the list!")
        break  # Stop the loop when number is found
else:
    # This else belongs to the for loop, executes if no break occurs
    print(f"{target} not found in the list.")