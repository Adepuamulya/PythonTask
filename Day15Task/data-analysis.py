# Data Analysis Tool (NumPy + Pandas) 
'''Scenario: 
Analyze student marks. 
Task: 
● Generate marks using NumPy 
● Convert into Pandas DataFrame 
● Use conditions to filter passing students 
● Calculate mean using math/NumPy 
● Use loop to print results'''
import numpy as np
import pandas as pd
marks = np.random.randint(30, 100, 5)
df = pd.DataFrame(marks, columns=["Marks"])
passed = df[df["Marks"] >= 50]
avg = np.mean(marks)
print("All Marks:")
print(df)
print("Passed Students:")
print(passed)
print("Average:", avg)
for m in marks:
    print("Mark:", m)