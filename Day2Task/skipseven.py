#Write a program that prints numbers from 1 to 10 but skips even numbers using continue
# Loop from 1 to 10
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num, end=" ")