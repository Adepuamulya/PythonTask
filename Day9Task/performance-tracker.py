# Performance Tracker (Decorators) 
#A software team wants to track how long functions take to execute. Create a decorator that measures and prints the execution time of a function.
import time

def performance_tracker(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end - start, "seconds")
    return wrapper

@performance_tracker
def task():
    for i in range(1000000):
        pass
    print("Task completed")

task()