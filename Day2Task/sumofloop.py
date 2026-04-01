#Write a program to find the sum of numbers from 1 to N using a loop
N = int(input("Enter a positive integer N: "))
total = 0
for i in range(1, N + 1):
    total += i
print(f"The sum of numbers from 1 to {N} is: {total}")
