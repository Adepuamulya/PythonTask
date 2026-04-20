# Temperature Monitoring System 
'''Scenario: 
temps = np.array([28, 30, 32, 35, 33, 31, 29]) 
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → daily temperature trend 
○ Bar chart → day-wise temperature 
○ Pie chart → proportion of high (>30) vs low temps 
○ Histogram → temperature frequency 
○ Scatter plot → day index vs temperature'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
df = pd.DataFrame({"Department": departments, "Salary": salaries})
plt.figure(figsize=(10, 6))

plt.subplot(2, 3, 1)
plt.plot(df["Salary"])
plt.title("Line")

plt.subplot(2, 3, 2)
plt.bar(df["Department"], df["Salary"])
plt.title("Bar")

plt.subplot(2, 3, 3)
plt.pie(df["Department"].value_counts(), labels=df["Department"].value_counts().index, autopct='%1.1f%%')
plt.title("Pie")

plt.subplot(2, 3, 4)
plt.hist(df["Salary"])
plt.title("Histogram")

plt.subplot(2, 3, 5)
plt.scatter(df.index, df["Salary"])
plt.title("Scatter")

plt.tight_layout()
plt.show()