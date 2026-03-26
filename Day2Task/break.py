#Write a program using break to stop printing numbers when the number reaches 5
# Print numbers from 1 onwards, but stop at 5
for num in range(1, 11):
    if num == 5:
        break 
     # Stop the loop when number reaches 5
    print(num)