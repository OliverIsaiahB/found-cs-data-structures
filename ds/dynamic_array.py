"""The array is the most fundamental data structure: a block of contiguous
memory you index by position. Python's `list` IS a dynamic array — it grows
itself as you append. Here we build a tiny one to see how that growth works."""
from __future__ import annotations


class DynamicArray:
    """A growable array backed by a fixed-capacity Python list.
    Doubling the capacity when full is what makes append amortized O(1)."""

    def __init__(self) -> None:
        self._capacity = 1
        self._size = 0
        self._data: list = [None] * self._capacity

    def __len__(self) -> int:
        return self._size

    def get(self, index: int) -> object:
        """Indexing is O(1): jump straight to the slot, no scanning."""
        if not 0 <= index < self._size:
            raise IndexError("index out of range")
        return self._data[index]

    def append(self, value: object) -> None:
        """Add to the end. When full, double the capacity first."""
        if self._size == self._capacity:
            self._grow()
        self._data[self._size] = value
        self._size += 1

    def _grow(self) -> None:
        self._capacity *= 2
        new_data = [None] * self._capacity
        for i in range(self._size):      # copy every element — O(n), but rare
            new_data[i] = self._data[i]
        self._data = new_data
