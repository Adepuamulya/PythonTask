#Write a Python program that generates 20 random numbers between 1 and 200 using 
#the random module and store them in a list. 
#Then using the math module, compute and display: 
# Maximum value 
# Minimum value 
# Square root of the maximum number 
# Logarithm of the minimum number 
import random
import math
numbers = []
for i in range(20):
    num = random.randint(1, 200)
    numbers.append(num)
max_value = max(numbers)
min_value = min(numbers)
sqrt_max = math.sqrt(max_value)
log_min = math.log(min_value)
print("Random Numbers:", numbers)
print("Maximum value:", max_value)
print("Minimum value:", min_value)
print("Square root of maximum number:", sqrt_max)
print("Logarithm of minimum number:", log_min)
