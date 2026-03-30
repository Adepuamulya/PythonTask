#Write a function that takes a string as input and returns the number of vowels. 
def count_vowels(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count += 1
    return count

text = input()
print(count_vowels(text))