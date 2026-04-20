#Monthly Sales Analysis 
'''Scenario: 
sales = np.array([100, 150, 200, 180, 220, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → sales trend 
○ Bar chart → month-wise comparison 
○ Pie chart → contribution of each month 
○ Histogram → frequency of sales values 
○ Scatter plot → month index vs sales '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
df = pd.DataFrame({"Month": months, "Sales": sales})
plt.figure(figsize=(10, 6))

plt.subplot(2, 3, 1)
plt.plot(df["Sales"])
plt.title("Line")

plt.subplot(2, 3, 2)
plt.bar(df["Month"], df["Sales"])
plt.title("Bar")

plt.subplot(2, 3, 3)
plt.pie(df["Sales"], labels=df["Month"], autopct='%1.1f%%')
plt.title("Pie")

plt.subplot(2, 3, 4)
plt.hist(df["Sales"])
plt.title("Histogram")

plt.subplot(2, 3, 5)
plt.scatter(df.index, df["Sales"])
plt.title("Scatter")

plt.tight_layout()
plt.show()