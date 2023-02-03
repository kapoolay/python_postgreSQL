class Book:
    TYPES= ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    # __repr__ method -> would allow us to include all of the data inside to recreate an object if we wanted to
    def __repr__(self):
        return f"<Book: {self.name}, {self.book_type}, weighing {self.weight}g>"

    # create a class that takes in a name/weight, but only type=hardcover
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)    # +100 bc it's hardcover

    # create a class that for just paperback
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


print(Book.TYPES)
# ('hardcover', 'paperback')

## init call
book = Book("Harry Potter", "hardcover", 1500)
print(book.name)
# Harry Potter

# repr call
print(book)
# <Book: Harry Potter, hardcover, weighing 1500g>

# hardcover call
book = Book.hardcover("Harry Potter", 1500)
print(book)
# <Book: Harry Potter, hardcover, weighing 1600g>

# paperback call
light = Book.paperback("Python 101", 600)
print(light)
# <Book: Python 101, paperback, weighing 600g>



