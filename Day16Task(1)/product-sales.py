#Product Sales & Profit Analysis 
'''Scenario: 
sales = np.array([200, 300, 250, 400, 350]) 
profit = np.array([50, 70, 60, 90, 80]) 
products = ["A", "B", "C", "D", "E"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → sales trend 
○ Bar chart → product vs sales 
○ Pie chart → sales contribution 
○ Histogram → profit distribution 
○ Scatter plot → sales vs profit'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

df = pd.DataFrame({"Dept": departments, "Salary": salaries})

plt.figure()

plt.subplot(2, 3, 1)
plt.plot(df["Salary"])
plt.title("Line")

plt.subplot(2, 3, 2)
plt.bar(df["Dept"], df["Salary"])
plt.title("Bar")

plt.subplot(2, 3, 3)
plt.pie(df["Dept"].value_counts(), labels=df["Dept"].value_counts().index, autopct='%1.1f%%')
plt.title("Pie")

plt.subplot(2, 3, 4)
plt.hist(df["Salary"])
plt.title("Hist")

plt.subplot(2, 3, 5)
plt.scatter(df.index, df["Salary"])
plt.title("Scatter")

plt.tight_layout()
plt.show()