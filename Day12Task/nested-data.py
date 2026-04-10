#Nested Data Independence (Deep Copy) 
'''A school stores classroom data: 
classes = [["Math", [30, 35]], ["Science", [25, 28]]] 
Scenario: 
● Create a deep copy of this structure. 
● Modify student count in original. 
Task: 
● Prove that copied data remains unchanged. 
● Explain why deep copy is required here. '''
import copy
classes = [["Math", [30, 35]], ["Science", [25, 28]]]
copy_classes = copy.deepcopy(classes)
classes[0][1][0] = 40
print("Original:", classes)
print("Deep Copy:", copy_classes)