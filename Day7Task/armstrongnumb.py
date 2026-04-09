#Armstrong Number 
#Write a program to check whether a given number is an Armstrong number or not. 
#Definition: A number is called an Armstrong number if the sum of the cubes of its digits is equal to the number itself. 
#Example: 
#Number = 153 
#Calculation: 
#1³ + 5³ + 3³ = 1 + 125 + 27 = 153 
#Output: 
#153 is an Armstrong number
num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
