#Store Sales Comparison 
'''Two stores record daily sales for 3 days. 
Scenario: 
Store A = [200, 250, 300] 
Store B = [180, 270, 310] 
Task: 
● Store them in NumPy arrays. 
● Find the daily difference in sales between the two stores. 
● Print the resulting array. '''
import numpy as np
storeA=[200,250,300]
storeB=[180,270,310]
a=np.array(storeA)
b=np.array(storeB)
difference=a-b
print("Daily Sales Difference:",difference)