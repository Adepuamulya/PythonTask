#Write a program to find the second largest number in a list
numbers = [10, 25, 5, 40, 15]

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest element:", second_largest)