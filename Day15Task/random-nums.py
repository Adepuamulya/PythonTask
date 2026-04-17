# Random Number Analyzer 
'''Scenario: 
A system generates random numbers for testing. 
Task: 
● Use random to generate 10 numbers 
● Store in a list 
● Use loop + condition to count even/odd numbers 
● Use set to remove duplicates '''
import random
nums = []
for i in range(10):
    nums.append(random.randint(1, 50))
even = 0
odd = 0
for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
unique_nums = set(nums)
print("Numbers:", nums)
print("Even count:", even)
print("Odd count:", odd)
print("Unique numbers:", unique_nums)