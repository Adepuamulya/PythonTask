# Temperature Monitoring System 
'''A weather station records temperatures for two days. 
Scenario: 
Day 1: [30, 32, 31] 
Day 2: [29, 33, 34] 
Task: 
● Create a 2D NumPy array to store this data. 
● Print the array. 
● Find the total temperature recorded'''
import numpy as np
temperatures = [[30, 32, 31],[29, 33, 34]]
temp_array = np.array(temperatures)
print("Temperature Array:")
print(temp_array)
total_temp = np.sum(temp_array)
print("Total Temperature Recorded:", total_temp)