#Find Maximum Value 
'''A dataset: 
arr = np.array([12, 45, 22, 67, 34]) 
Task: 
● Convert to Pandas Series 
● Find the maximum value '''
import numpy as np
import pandas as pd
arr = np.array([12, 45, 22, 67, 34])
S = pd.Series(arr)
max_value = S.max()
print(S)
print("\nMaximum value:")
print(max_value)