#Write a program using continue to skip printing the number 3 in a loop from 1 to 10.
# Loop from 1 to 10
for num in range(1, 11):
    if num == 3:
        continue  # Skip the rest of the loop for num = 3
    print(num, end=" ")