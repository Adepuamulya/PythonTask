#Write a program to find the sum of numbers from 1 to N using a loop
# Ask the user to enter a number N
N = int(input("Enter a positive integer N: "))

# Initialize sum
total = 0

# Use a for loop to add numbers from 1 to N
for i in range(1, N + 1):
    total += i

# Display the result
print(f"The sum of numbers from 1 to {N} is: {total}")