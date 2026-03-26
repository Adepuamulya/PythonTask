#Write a program to perform left shift (<<) and right shift (>>) operations on a number
# Ask the user to enter a number
num = int(input("Enter a number: "))

# Ask the user to enter the number of positions to shift
shift = int(input("Enter the number of positions to shift: "))

# Perform left shift
left_shift_result = num << shift

# Perform right shift
right_shift_result = num >> shift

# Display the results
print(f"{num} << {shift} = {left_shift_result}")
print(f"{num} >> {shift} = {right_shift_result}")