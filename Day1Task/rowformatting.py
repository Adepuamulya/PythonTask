#Print a table row using formatted strings
# Sample data
item = "Shirt"
quantity = 5
price = 499.75

# Printing a table row using f-strings with alignment
print(f"{'Item':<10} {'Quantity':<10} {'Price':>10}")
print(f"{item:<10} {quantity:<10} ${price:>9.2f}")