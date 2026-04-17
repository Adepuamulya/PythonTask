# Basic File Logger 
'''Scenario: 
A system logs user actions. 
Task: 
● Take user input 
● Store logs in a file 
● Use loop to allow multiple entries 
● Handle file errors using exception handling'''
while True:
    try:
        f = open("log.txt", "a")
        text = input("Enter log (type okay to stop): ")
        if text == "okay":
            f.close()
            break
        f.write(text + "\n")
        f.close()
    except:
        print("File error")
print("Logs saved")