# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:30:01 2024

@author: belgu
"""

# -- coding: utf-8 --
"""
Created on Tue Feb 13 13:40:50 2024

@author: belgu
"""

class Library:
    def init(self):
        self.file = open("books.txt", "a+")

    def del(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            book_info = book.strip().split(',')
            print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        removed = False
        for book in books:
            if title not in book:
                updated_books.append(book)
            else:
                removed = True
        if removed:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(updated_books)
            print("Book removed successfully.")
        else:
            print("Book not found.")


# Create Library object
lib = Library()

# Menu
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")