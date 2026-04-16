#Student Marks DataFrame Analysis 
'''A DataFrame: 
data = pd.DataFrame({ 
"Name": ["A", "B", "C"], 
"Math": [80, 70, 60], 
"Science": [90, 60, 70] 
}) 
Task: 
● Add a new column Total = Math + Science 
● Find the student with the highest total marks '''
import pandas as pd
#Create DataFrame
data = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Math": [80, 70, 60],
    "Science": [90, 60, 70]
})
#Add Total
data["Total"] = data["Math"] + data["Science"]
#highest total
top_student = data.loc[data["Total"].idxmax()]
#results
print("DataFrame with Total:")
print(data)
print("\nStudent with highest total marks:")
print(top_student)