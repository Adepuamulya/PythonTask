#Notes Reader Program 
#A student stores daily notes in a file called notes.txt. Write a program that opens the file, reads all the contents, and displays them on the screen. 
file = open("notes.txt", "r")
content = file.read()
print("Notes:")
print(content)
file.close()