# Library Management System (Constructor & Inheritance) 
#A library stores information about books and digital books. Create a base class Book 
#with a constructor to initialize book details. Create a derived class EBook that adds file size information. 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def show_book(self):
        print("Title:", self.title)
        print("Author:", self.author)
class EBook(Book):
    def __init__(self, title, author, size):
        Book.__init__(self, title, author)
        self.size = size

    def show_ebook(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("File Size:", self.size, "MB")
ebook = EBook("Python", "Ammu", 4)
ebook.show_ebook()
