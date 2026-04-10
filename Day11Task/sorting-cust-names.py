#Sorting Customer Names 
'''A system stores customer names: 
["Ravi", "Anil", "Sita", "John"] 
Task: 
● Convert it to a NumPy array. 
● Sort the names alphabetically.'''
import numpy as np
names=np.array(["Ravi","Anil","Sita","John"])
sorted_names=np.sort(names)
print(sorted_names)