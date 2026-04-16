# Row Selection & Deletion 
'''A DataFrame: 
df = pd.DataFrame({ 
"A": [10, 20, 30], 
"B": [5, 15, 25] 
}, index=["x", "y", "z"]) 
Task: 
● Select row with index "y" 
● Delete row "x" 
● Print updated DataFrame'''
import pandas as pd
df = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [5, 15, 25]
},
index=["x", "y", "z"])
row_y = df.loc["y"]
print("Row with index 'y':")
print(row_y)
df = df.drop("x")
print("\nUpdated DataFrame:")
print(df)
