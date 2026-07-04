"""A linked list strings values together with pointers instead of storing them
contiguously. Each node holds a value and a reference to the next node. The
trade-off versus an array: O(1) insertion at the front, but O(n) to reach the
i-th element (you must walk the chain — no jumping)."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    value: object
    next: "Node | None" = None


class LinkedList:
    def __init__(self) -> None:
        self._head: Node | None = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def prepend(self, value) -> None:
        """Add to the front — O(1): just point the new node at the old head."""
        self._head = Node(value, self._head)
        self._size += 1

    def get(self, index: int) -> object:
        """Walk to the i-th node — O(n). No random access like an array."""
        if not 0 <= index < self._size:
            raise IndexError("index out of range")
        node = self._head
        for _ in range(index):
            node = node.next
        return node.value

    def to_list(self) -> list:
        out, node = [], self._head
        while node is not None:
            out.append(node.value)
            node = node.next
        return out
