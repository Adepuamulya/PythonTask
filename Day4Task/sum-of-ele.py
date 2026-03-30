#Write a function to find the sum of elements in a list using a user-defined function
def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total

numbers = [1, 2, 3, 4, 5]
print(sum_list(numbers))