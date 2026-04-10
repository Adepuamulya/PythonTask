# Copy vs View Behavior in Data Processing 
'''Scenario: 
A dataset: 
[10, 20, 30, 40] 
Task: 
● Create a copy of the array. 
● Modify the original array. 
● Show that the copy does not change. 
● Repeat using view() and observe the difference.'''
import numpy as np
data=np.array([10,20,30,40])
# Copy
copy_arr=data.copy()
data[0]=100
print("Original:",data)
print("Copy:",copy_arr)
# View
data2=np.array([10,20,30,40])
view_arr=data2.view()
data2[0]=100
print("Original with view:",data2)
print("View:",view_arr)