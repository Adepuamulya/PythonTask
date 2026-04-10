#Combine Two Sensor Readings 
'''Two sensors record readings during a test. 
Scenario: 
Sensor1 = [10, 20, 30] 
Sensor2 = [40, 50, 60] 
Task: 
● Store both readings in NumPy arrays. 
● Combine them into one array using NumPy concatenation. '''
import numpy as np
sensor1=[10,20,30]
sensor2=[40,50,60]
array1=np.array(sensor1)
array2=np.array(sensor2)
combined=np.concatenate((array1,array2))
print("Combined Array:",combined)