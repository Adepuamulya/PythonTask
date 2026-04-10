# Multi-Department Data Aggregation 
'''A company collects employee counts from two branches. 
Branch A: 
[[10, 20], 
[30, 40]] 
Branch B: 
[[5, 15], 
[25, 35]] 
Scenario: 
● Combine the two matrices. 
● Calculate the total employees across all departments. 
● Print the combined matrix and total.'''
import numpy as np
branchA=[[10,20],[30,40]]
branchB=[[5,15],[25,35]]
a=np.array(branchA)
b=np.array(branchB)
combined=a+b
total=np.sum(combined)
print("Combined Matrix:")
print(combined)
print("Total Employees:",total)