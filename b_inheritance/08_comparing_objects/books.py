from functools import total_ordering
from __future__ import annotations


@total_ordering
class Book:
    def __init__(self, title: str, author:str):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"\'{self.title}\' by {self.author}"

    def __eq__(self, other: Book) -> type(NotImplemented) | bool:
        if not isinstance(other, Book):
            return NotImplemented
        if self.author != other.author:
            return False
        if self.title != other.title:
            return False

        return True

    def __ne__(self, other: Book) -> type(NotImplemented) | bool:
        return not self == other

    def __lt__(self, other: Book) -> type(NotImplemented) | bool:
        if not isinstance(other, Book):
            return NotImplemented
        else:
            return self.title < other.title
