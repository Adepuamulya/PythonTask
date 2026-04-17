#Shopping Cart System 
'''Scenario: A user adds items to a shopping cart. 
Task: 
● Store items in a list 
● Convert to set to remove duplicates 
● Use loop + condition to calculate total cost 
● Handle invalid input using try-except'''
items = []
prices = []
for i in range(3):
    item = input("Enter item: ")
    try:
        price = float(input("Enter price: "))
        items.append(item)
        prices.append(price)
    except:
        print("Invalid price")
unique_items = set(items)
total = 0
for p in prices:
    if p > 0:
        total += p
print("Items:", items)
print("Unique Items:", unique_items)
print("Total Cost:", total)