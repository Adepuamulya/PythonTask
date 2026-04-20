# Combined Visualization Dashboard 
'''Scenario: 
sales = np.array([100, 200, 150, 300]) 
products = ["A", "B", "C", "D"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph (trend) 
○ Bar chart (comparison) 
○ Pie chart (distribution) 
● Show all in single figure (subplots)'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]
df = pd.DataFrame({"Product": products, "Sales": sales})
plt.figure()
plt.subplot(1, 3, 1)
plt.plot(df["Product"], df["Sales"], marker='o')
plt.title("Line")
plt.subplot(1, 3, 2)
plt.bar(df["Product"], df["Sales"])
plt.title("Bar")
plt.subplot(1, 3, 3)
plt.pie(df["Sales"], labels=df["Product"], autopct='%1.1f%%')
plt.title("Pie")
plt.tight_layout()
plt.show()