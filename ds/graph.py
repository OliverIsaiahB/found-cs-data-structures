"""A graph is the most general structure: nodes (vertices) connected by edges —
any relationships, including cycles. We store it as an ADJACENCY LIST: each node
mapped to its neighbors. BFS (a queue) explores by distance; DFS (a stack /
recursion) plunges deep. Both visit every node and edge once: O(V + E)."""
from __future__ import annotations

from collections import deque


class Graph:
    def __init__(self) -> None:
        self._adj: dict[object, list] = {}

    def add_edge(self, u, v) -> None:
        """Add an undirected edge u—v by recording each as the other's neighbor."""
        self._adj.setdefault(u, []).append(v)
        self._adj.setdefault(v, []).append(u)

    def neighbors(self, u) -> list:
        return self._adj.get(u, [])

    def bfs(self, start) -> list:
        """Breadth-first: visit by rings of increasing distance, using a QUEUE."""
        visited = {start}
        order: list = []
        q: deque = deque([start])
        while q:
            node = q.popleft()
            order.append(node)
            for nbr in self._adj.get(node, []):
                if nbr not in visited:   # the visited set stops cycles looping forever
                    visited.add(nbr)
                    q.append(nbr)
        return order

    def dfs(self, start) -> list:
        """Depth-first: plunge down each path before backtracking, via RECURSION."""
        visited: set = set()
        order: list = []

        def visit(node) -> None:
            visited.add(node)
            order.append(node)
            for nbr in self._adj.get(node, []):
                if nbr not in visited:
                    visit(nbr)

        visit(start)
        return order
