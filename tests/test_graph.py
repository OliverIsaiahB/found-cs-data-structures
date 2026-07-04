from ds.graph import Graph


def build():
    g = Graph()
    for u, v in [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]:
        g.add_edge(u, v)
    return g


def test_bfs_visits_nearer_first():
    g = build()
    order = g.bfs(0)
    assert order[0] == 0                  # starts at the source
    assert set(order) == {0, 1, 2, 3, 4}  # reaches every node
    assert order.index(1) < order.index(4)  # distance-1 before distance-2


def test_dfs_visits_all():
    g = build()
    assert sorted(g.dfs(0)) == [0, 1, 2, 3, 4]


def test_isolated_node():
    g = Graph()
    g.add_edge(0, 1)
    assert g.bfs(2) == [2]                # a node with no edges visits only itself
