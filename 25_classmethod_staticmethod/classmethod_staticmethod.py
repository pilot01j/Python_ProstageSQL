class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called the class_method of {cls}")

    @staticmethod
    def static_method():
        print(f"Called the static_method.")

test = ClassTest()
print(test.instance_method())
print(test.class_method())
print(test.static_method())
print("------------------------------------------------------------------")

class Book:
    TYPE = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book: {self.name}, {self.book_type}, weighting {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPE[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPE[1], page_weight + 200)

print(Book.TYPE)
book = Book("Harry Potter", "hardcover", 1500)
print(book.name)
print(book)
print("------------------------------------------------------------------")
book = Book.hardcover("Harry Potter", 1500)
print(book)
print("------------------------------------------------------------------")
book = Book.paperback("Harry Potter", 1500)
print(book)
