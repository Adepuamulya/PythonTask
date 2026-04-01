#Write a program to print all even numbers between 1 and 50
print("Even numbers between 1 and 50:")
for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=" ")
