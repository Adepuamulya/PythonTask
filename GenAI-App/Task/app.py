class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "issued": False
        }

        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n===== BOOK LIST =====")
        for book in self.books:
            status = "Issued" if book["issued"] else "Available"

            print(f"""
Book ID : {book['id']}
Title   : {book['title']}
Author  : {book['author']}
Status  : {status}
---------------------------
""")

    def search_book(self):
        title = input("Enter book title to search: ")

        found = False

        for book in self.books:
            if title.lower() in book["title"].lower():
                print("\nBook Found")
                print("ID:", book["id"])
                print("Title:", book["title"])
                print("Author:", book["author"])
                found = True

        if not found:
            print("Book not found.")

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")

        for book in self.books:
            if book["id"] == book_id:
                if book["issued"]:
                    print("Book already issued.")
                else:
                    book["issued"] = True
                    print("Book issued successfully.")
                return

        print("Book not found.")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        for book in self.books:
            if book["id"] == book_id:
                if not book["issued"]:
                    print("Book is already available.")
                else:
                    book["issued"] = False
                    print("Book returned successfully.")
                return

        print("Book not found.")

    def delete_book(self):
        book_id = input("Enter Book ID to delete: ")

        for book in self.books:
            if book["id"] == book_id:
                self.books.remove(book)
                print("Book deleted successfully.")
                return

        print("Book not found.")


def main():
    library = Library()

    while True:
        print("""
========== LIBRARY MANAGEMENT SYSTEM ==========
1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit
==============================================
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            library.search_book()

        elif choice == "4":
            library.issue_book()

        elif choice == "5":
            library.return_book()

        elif choice == "6":
            library.delete_book()

        elif choice == "7":
            print("Thank you for using Library Management System.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()