"""A queue is First-In-First-Out (FIFO): the first thing in line is served first,
like people queuing. The catch: removing from the FRONT of a plain list is O(n)
because every other element must shift left. We use a deque to keep it O(1)."""
from __future__ import annotations

from collections import deque


class Queue:
    def __init__(self) -> None:
        self._items: deque = deque()

    def __len__(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def enqueue(self, value: object) -> None:
        """Add to the back of the line — O(1)."""
        self._items.append(value)

    def dequeue(self) -> object:
        """Remove and return the front of the line — O(1) with a deque."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def front(self) -> object:
        """Look at the front without removing it."""
        if self.is_empty():
            raise IndexError("front of empty queue")
        return self._items[0]
