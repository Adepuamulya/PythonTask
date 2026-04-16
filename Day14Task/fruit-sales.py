#Fruit Sales Comparison (Series Addition) 
'''A shop tracks fruit sales: 
S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"]) 
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"]) 
Task: 
● Add both series 
● Find the total sales of all fruits combined'''
import pandas as pd
#Series
S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"])
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])
print("S1:")
print(S1)
print("\nS2:")
print(S2)