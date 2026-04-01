#Write a program that searches for a number in a list and breaks the loop when found.
numbers = [4, 7, 1, 9, 12, 5]
target = int(input("Enter the number to search: "))
for num in numbers:
    if num == target:
        print(f"{target} found in the list!")
        break 
else:
    print(f"{target} not found in the list.")
