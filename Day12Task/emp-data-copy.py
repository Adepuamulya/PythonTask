# Employee Data Copy Issue (Shallow vs Deep Copy) 
'''A company stores employee data: 
employees = [[101, "A"], [102, "B"], [103, "C"]] 
Scenario: 
● Create a shallow copy of the list. 
● Modify one nested list (e.g., change "A" to "Z"). 
● Observe changes in both lists. 
Task: 
● Explain why the change reflects in both. 
● Fix it using deep copy.'''
# Shallow copy
import copy
employees = [[101, "A"], [102, "B"], [103, "C"]]
shallow_copy = employees.copy()
shallow_copy[0][1] = "Z"
print("Employees:", employees)
print("Shallow Copy:", shallow_copy)

# Deep copy
import copy
employees = [[101, "A"], [102, "B"], [103, "C"]]
deep_copy = copy.deepcopy(employees)
deep_copy[0][1] = "Z"
print("Employees:", employees)
print("Deep Copy:", deep_copy)

