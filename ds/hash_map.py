"""A hash map stores key→value pairs and finds a key in amortized O(1). The idea:
a hash function turns a key into a bucket index; you only search that one small
bucket, not the whole structure. Collisions (two keys, same bucket) are handled
here by 'separate chaining' — each bucket holds a small list of pairs."""
from __future__ import annotations


class HashMap:
    def __init__(self, capacity: int = 8) -> None:
        self._capacity = capacity
        self._size = 0
        self._buckets: list[list] = [[] for _ in range(capacity)]

    def __len__(self) -> int:
        return self._size

    def _index(self, key) -> int:
        """Hash the key, then fold it into a valid bucket index."""
        return hash(key) % self._capacity

    def put(self, key, value) -> None:
        """Insert or update. Average O(1); resizes to keep buckets short."""
        bucket = self._buckets[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value          # key exists → update in place
                return
        bucket.append([key, value])      # new key → append to the chain
        self._size += 1
        if self._size > self._capacity:  # load factor > 1 → grow
            self._resize()

    def get(self, key):
        """Look up a key. Search only its bucket, not the whole map."""
        bucket = self._buckets[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)

    def _resize(self) -> None:
        old = [p for b in self._buckets for p in b]
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for key, value in old:           # rehash every pair into the bigger table
            self.put(key, value)
