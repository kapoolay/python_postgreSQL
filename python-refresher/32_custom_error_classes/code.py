## Assigning the 'ValueError' class to a custom error class called 'TooManyPagesReadError'
class TooManyPagesReadError(ValueError):
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    ## repr method
    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}"
        )

    ## pages read method
    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"ERROR: You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages."
            )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}.")


python101 = Book("Python101", 50)
python101.read(37)
python101.read(50)
'''
You have now read 37 pages out of 50.
Traceback (most recent call last):
  File "/Users/Kev/learning/Udemy/python_postgreSQL/python-refresher/32_custom_error_classes/code.py", line 27, in <module>
    python101.read(50)
  File "/Users/Kev/learning/Udemy/python_postgreSQL/python-refresher/32_custom_error_classes/code.py", line 18, in read
    raise TooManyPagesReadError(
__main__.TooManyPagesReadError: You tried to reach 87 pages, but this book only has 50 pages.
'''

## Using try and except
# This is used to print something nice and clean for the user to read, rather than the error message printed out above in the 'python101.read(50)'
html101 = Book("HTML 101", 100)

try:
    html101.read(40)
    html101.read(75)
except TooManyPagesReadError as e:
    print(e)

'''
You have now read 40 pages out of 100.
ERROR: You tried to read 115 pages, but this book only has 100 pages.
'''
