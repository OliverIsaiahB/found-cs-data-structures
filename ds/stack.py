"""A stack is a Last-In-First-Out (LIFO) collection: the last thing you put in
is the first thing you take out — like a stack of plates. Built on a list, every
operation is O(1) at the end of the array."""
from __future__ import annotations


class Stack:
    def __init__(self) -> None:
        self._items: list = []

    def __len__(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def push(self, value: object) -> None:
        """Add to the top — O(1) append at the end of the list."""
        self._items.append(value)

    def pop(self) -> object:
        """Remove and return the top item. Errors if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> object:
        """Look at the top without removing it."""
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._items[-1]
