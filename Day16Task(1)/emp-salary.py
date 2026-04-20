# Employee Salary Insights 
'''Scenario: 
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000]) 
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"] 
Task: 
● Convert into DataFrame 
● Plot: 
○ Line graph → salary trend 
○ Bar chart → department-wise salary comparison 
○ Pie chart → department distribution 
○ Histogram → salary distribution 
○ Scatter plot → index vs salary '''
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