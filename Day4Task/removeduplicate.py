#Write a program to remove duplicate characters from a string
s = input()
result = ""
for i in s:
    if i not in result:
        result += i
print(result)
