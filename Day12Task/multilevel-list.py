# Multi-Level List Transformation (Advanced List Comprehension) 
'''A dataset contains: 
data = [[1, 2, 3], [4, 5], [6]] 
Task: 
● Flatten the list using list comprehension. 
● Then create a new list containing squares of only even numbers.'''
data = [[1, 2, 3], [4, 5], [6]]
flat = [x for sub in data for x in sub]
result = [x**2 for x in flat if x % 2 == 0]
print(flat)
print(result)