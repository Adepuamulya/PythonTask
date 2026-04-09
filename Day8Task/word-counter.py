#Word Counter Program 
#A writer saves an article in a file called article.txt. Write a Python program that: 
#● Opens and reads the file 
#● Counts the number of words, lines, and characters in the file 
#● Displays the results.
file = open("article.txt", "r")
content = file.read()
words = len(content.split())
characters = len(content)
file.seek(0)
lines = len(file.readlines())
file.close()
print("Number of words:", words)
print("Number of lines:", lines)
print("Number of characters:", characters) 
