#Complex DataFrame Transformation 
'''A DataFrame: 
df = pd.DataFrame({ 
"Name": ["A", "B", "C", "D"], 
"Marks": [50, 80, 30, 90] 
}) 
Scenario: 
● Students scoring below 50 failed 
Task: 
1. Create a column Status ("Pass"/"Fail") 
2. Filter only passed students 
3. Calculate average marks of passed students'''
import pandas as pd
df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})
df["Status"] = ["Pass" if x >= 50 else "Fail" for x in df["Marks"]]
passed_students = df[df["Status"] == "Pass"]
average_marks = passed_students["Marks"].mean()
print(df)
print("\nPassed Students:")
print(passed_students)
print("\nAverage Marks of Passed Students:")
print(average_marks)