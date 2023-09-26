from typing import List


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


print(list_avg([1, 2]))
print("------------------------------------------------------------------")


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count


print("------------------------------------------------------------------")


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."
