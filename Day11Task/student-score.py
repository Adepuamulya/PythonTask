#Splitting Student Scores Across Servers 
'''A dataset: 
[50, 60, 70, 80, 90, 100, 110, 120] 
Scenario: 
A distributed system needs to divide this data among 4 servers. 
Task: 
● Convert to NumPy array. 
● Split the array into 4 equal parts using array_split().'''
import numpy as np
data=np.array([50,60,70,80,90,100,110,120])
parts=np.array_split(data,4)
print(parts)