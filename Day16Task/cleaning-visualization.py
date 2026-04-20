#Data Cleaning + Visualization 
'''Scenario: 
data = np.array([100, np.nan, 200, 150, np.nan, 300]) 
Task: 
1. Convert to Pandas Series 
2. Replace NaN with mean 
3. Plot: 
○ Line graph of cleaned data 
○ Bar chart of values > average'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = np.array([100, np.nan, 200, 150, np.nan, 300])
series = pd.Series(data)
mean_value = series.mean()
series = series.fillna(mean_value)
plt.figure()
plt.subplot(1, 2, 1)
plt.plot(series, marker='o')
plt.title("Cleaned Data Line")
filtered = series[series > mean_value]
plt.subplot(1, 2, 2)
plt.bar(filtered.index.astype(str), filtered.values)
plt.title("Values > Average")
plt.tight_layout()
plt.show()