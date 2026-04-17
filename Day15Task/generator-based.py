# Generator-based Log Reader 
'''Scenario: 
A large log file needs to be processed. 
Task: 
● Create a generator to read file line by line 
● Use loop to process logs 
● Use condition to filter errors 
● Count occurrences using a dictionary '''
def read_logs(file):
    with open(file, "r") as f:
        for line in f:
            yield line
error_count = {}
for line in read_logs("log.txt"):
    if "error" in line.lower():
        line = line.strip()
        if line in error_count:
            error_count[line] += 1
        else:
            error_count[line] = 1
if error_count:
    for k in error_count:
        print(k, ":", error_count[k])
else:
    print("No errors found")