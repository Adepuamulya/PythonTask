# Smart Data Processing Pipeline 
'''Scenario: 
A system processes numeric data from file. 
Task: 
● Read numbers from a file 
● Use NumPy for calculations (mean, std) 
● Convert results to Pandas DataFrame 
● Use exception handling for bad data 
● Use a generator to stream data 
● Apply decorator to measure execution time'''
import numpy as np
import pandas as pd
import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        print("Time:", time.time() - start)
    return wrapper
def read_file():
    with open("data.txt") as f:
        for line in f:
            try:
                yield float(line)
            except:
                pass
@timer
def main():
    data = list(read_file())    
    if not data:
        print("No data")
        return
    df = pd.DataFrame({
        "Mean": [np.mean(data)],
        "Std": [np.std(data)]
    })
    print(df)
main()