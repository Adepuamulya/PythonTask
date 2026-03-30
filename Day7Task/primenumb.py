#Prime Number 
#Question: Write a program to check whether a number is Prime. 
#Definition: A Prime number is a number that has only two factors: 1 and itself. 
#Example: 
#Number = 7 
#Output: 
#Factors = 1, 7 
#7 is a Prime number
num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")