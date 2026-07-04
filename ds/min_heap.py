"""A binary heap is a complete binary tree stored in a plain array, kept so that
every parent is <= its children (a MIN-heap). That lets you read the smallest
element in O(1) and push/pop in O(log n). It's how a priority queue is built."""
from __future__ import annotations


class MinHeap:
    def __init__(self) -> None:
        self._data: list[int] = []

    def __len__(self) -> int:
        return len(self._data)

    def peek_min(self) -> int:
        """The minimum is always at the root — index 0 — so this is O(1)."""
        if not self._data:
            raise IndexError("peek at empty heap")
        return self._data[0]

    def push(self, value: int) -> None:
        """Add at the end, then sift up to restore the heap property — O(log n)."""
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def pop_min(self) -> int:
        """Remove the root: swap it with the last item, shrink, sift down — O(log n)."""
        if not self._data:
            raise IndexError("pop from empty heap")
        self._data[0], self._data[-1] = self._data[-1], self._data[0]
        smallest = self._data.pop()
        if self._data:
            self._sift_down(0)
        return smallest

    def _sift_up(self, i: int) -> None:
        while i > 0:
            parent = (i - 1) // 2        # parent index in the array layout
            if self._data[i] >= self._data[parent]:
                break                    # heap property satisfied
            self._data[i], self._data[parent] = self._data[parent], self._data[i]
            i = parent

    def _sift_down(self, i: int) -> None:
        n = len(self._data)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            smallest = i
            if left < n and self._data[left] < self._data[smallest]:
                smallest = left
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right
            if smallest == i:
                break
            self._data[i], self._data[smallest] = self._data[smallest], self._data[i]
            i = smallest
