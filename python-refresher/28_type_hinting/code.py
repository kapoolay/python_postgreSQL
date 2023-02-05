def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

list_avg(123)

## Example with type hinting

class Book:
    TYPES= ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    # __repr__ method -> would allow us to include all of the data inside to recreate an object if we wanted to
    def __repr__(self) -> str:
        return f"<Book: {self.name}, {self.book_type}, weighing {self.weight}g>"

    # create a class that takes in a name/weight, but only type=hardcover
    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)    # +100 bc it's hardcover

    # create a class that for just paperback
    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)