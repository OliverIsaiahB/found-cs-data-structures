"""A doubly linked list gives each node a 'prev' pointer as well as 'next', and
the list tracks a tail. That buys O(1) insertion at BOTH ends and lets you walk
backwards. It's the structure behind deques and LRU caches."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DNode:
    value: object
    prev: "DNode | None" = None
    next: "DNode | None" = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self._head: DNode | None = None
        self._tail: DNode | None = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def append(self, value) -> None:
        """Add at the tail — O(1) thanks to the tail pointer."""
        node = DNode(value, prev=self._tail)
        if self._tail is not None:
            self._tail.next = node       # old tail points forward to new node
        else:
            self._head = node            # empty list: new node is also the head
        self._tail = node
        self._size += 1

    def prepend(self, value) -> None:
        """Add at the head — also O(1)."""
        node = DNode(value, next=self._head)
        if self._head is not None:
            self._head.prev = node       # old head points back to new node
        else:
            self._tail = node
        self._head = node
        self._size += 1

    def to_list_forward(self) -> list:
        out, node = [], self._head
        while node is not None:
            out.append(node.value)
            node = node.next
        return out

    def to_list_backward(self) -> list:
        out, node = [], self._tail
        while node is not None:
            out.append(node.value)
            node = node.prev
        return out
