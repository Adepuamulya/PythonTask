# Student Performance Dashboard 
'''Scenario: 
A school records marks of students in one subject: 
marks = np.array([45, 67, 89, 56, 72, 91, 38]) 
students = ["A", "B", "C", "D", "E", "F", "G"] 
Task: 
● Convert to Pandas DataFrame 
● Plot: 
○ Line graph → trend of marks 
○ Bar chart → student vs marks 
○ Pie chart → Pass (>50) vs Fail 
○ Histogram → distribution of marks 
○ Scatter plot → index vs marks '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]
df = pd.DataFrame({"Student": students, "Marks": marks})
plt.figure(figsize=(10, 6))

plt.subplot(2, 3, 1)
plt.plot(df["Marks"])
plt.title("Line")

plt.subplot(2, 3, 2)
plt.bar(df["Student"], df["Marks"])
plt.title("Bar")

plt.subplot(2, 3, 3)
plt.pie([sum(df["Marks"] > 50), sum(df["Marks"] <= 50)], labels=["Pass", "Fail"], autopct='%1.1f%%')
plt.title("Pie")

plt.subplot(2, 3, 4)
plt.hist(df["Marks"])
plt.title("Histogram")

plt.subplot(2, 3, 5)
plt.scatter(df.index, df["Marks"])
plt.title("Scatter")
plt.tight_layout()
plt.show()