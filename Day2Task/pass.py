#Write a program that uses pass inside a loop
# Loop from 1 to 5
for num in range(1, 6):
    if num == 3:
        pass  # Do nothing when num is 3
    print(num, end=" ")