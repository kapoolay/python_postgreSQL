'''
Inheritance: A book has a bookshelf
Composition: A bookshelf has many books
'''

class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book: {self.name}"

book1 = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book1, book2)

print(book1)        # Book: Harry Potter
print(book2)        # Book: Python 101
print(shelf)        # BookShelf with 2 books.
print(shelf.books[0])       # Book: Harry Potter
print(shelf.books[1])       # Book: Python 101


