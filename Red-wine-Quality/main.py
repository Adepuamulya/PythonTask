import pandas as pd

# Read CSV file directly
df = pd.read_csv("winequality-red.csv")

# Show first 5 rows
print(df.head())

# Show shape
print(df.shape)

# Show column names
print(df.columns)