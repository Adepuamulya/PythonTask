# Palindrome Number 
#Question: Write a program to check whether a number is a Palindrome. 
#Definition: A number is a Palindrome if it reads the same forward and backward. 
#Example: 
#Number = 121 
#Reverse = 121 
#Output: 
#121 is a Palindrome number
num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10
if num == rev:
    print(num, "is a Palindrome number")
else:
    print(num, "is not a Palindrome number")
