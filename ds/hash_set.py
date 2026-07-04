"""A set stores unique values and answers one question fast: 'is X in here?' in
amortized O(1). It's a hash map that only cares about keys — no values. Use a set
for de-duplication, 'have I seen this?', and membership-heavy work."""
from __future__ import annotations


class HashSet:
    def __init__(self, capacity: int = 8) -> None:
        self._capacity = capacity
        self._size = 0
        self._buckets: list[list] = [[] for _ in range(capacity)]

    def __len__(self) -> int:
        return self._size

    def _index(self, value) -> int:
        return hash(value) % self._capacity

    def add(self, value) -> None:
        """Add a value if absent; duplicates are silently ignored."""
        bucket = self._buckets[self._index(value)]
        if value in bucket:              # already present → do nothing
            return
        bucket.append(value)
        self._size += 1

    def contains(self, value) -> bool:
        """Membership test — search only the value's bucket."""
        return value in self._buckets[self._index(value)]

    def union(self, other: "HashSet") -> "HashSet":
        """All values in either set."""
        result = HashSet()
        for bucket in self._buckets:
            for v in bucket:
                result.add(v)
        for bucket in other._buckets:
            for v in bucket:
                result.add(v)
        return result
