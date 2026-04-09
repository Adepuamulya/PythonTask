#Write a program to check whether a string is a palindrome
s = input()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
