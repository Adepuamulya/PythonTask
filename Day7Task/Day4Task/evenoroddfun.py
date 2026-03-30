# Write a function to check whether a number is even or odd
def check(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

n = int(input())
check(n)