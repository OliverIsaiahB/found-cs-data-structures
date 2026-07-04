"""A binary search tree keeps values ordered: for every node, smaller values go
left, larger go right. That ordering turns search into repeated halving — O(h),
the height — and an in-order walk emits the values in SORTED order."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    value: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


class BST:
    def __init__(self) -> None:
        self._root: TreeNode | None = None

    def insert(self, value: int) -> None:
        """Descend left/right by comparison until an empty slot is found — O(h)."""
        self._root = self._insert(self._root, value)

    def _insert(self, node: TreeNode | None, value: int) -> TreeNode:
        if node is None:
            return TreeNode(value)       # found the empty slot
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node                      # equal values ignored (no duplicates)

    def contains(self, value: int) -> bool:
        """Search by halving: go left or right, discarding the other subtree."""
        node = self._root
        while node is not None:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

    def in_order(self) -> list[int]:
        """Left, node, right — yields the values in SORTED order on a BST."""
        out: list[int] = []
        self._in_order(self._root, out)
        return out

    def _in_order(self, node: TreeNode | None, out: list[int]) -> None:
        if node is None:
            return
        self._in_order(node.left, out)
        out.append(node.value)
        self._in_order(node.right, out)
