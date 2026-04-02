#Infinite Even Number Generator (Generators) 
#Create a generator function that continuously generates even numbers starting from 
#2. The program should print the first N even numbers using this generator. 
def even_generator():
    num = 2
    while True:
        yield num
        num += 2

gen = even_generator()

n = int(input("Enter how many even numbers to print: "))

for i in range(n):
    print(next(gen))