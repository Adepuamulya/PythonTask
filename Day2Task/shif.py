#Write a program to perform left shift (<<) and right shift (>>) operations on a number
num = int(input("Enter a number: "))
shift = int(input("Enter the number of positions to shift: "))
left_shift_result = num << shift
right_shift_result = num >> shift
print(f"{num} << {shift} = {left_shift_result}")
print(f"{num} >> {shift} = {right_shift_result}")
