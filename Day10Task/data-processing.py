# Data Processing Pipeline 
'''A data pipeline receives the following array: 
[12, 7, 25, 3, 18, 10] 
Scenario: 
1. Convert the list into a NumPy array. 
2. Sort the array. 
3. Split the sorted array into two equal parts. 
4. Calculate the sum of each part. 
Output: 
● Sorted array 
● Two split arrays 
● Sum of each part'''
import numpy as np
data=[12,7,25,3,18,10]
arr=np.array(data)
sorted_arr=np.sort(arr)
parts=np.split(sorted_arr,2)
sum1=np.sum(parts[0])
sum2=np.sum(parts[1])
print("Sorted Array:",sorted_arr)
print("First Part:",parts[0])
print("Second Part:",parts[1])
print("Sum of First Part:",sum1)
print("Sum of Second Part:",sum2)