#Write a program to count the frequency of each character in a string
s = input()
freq = {}

for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)