from ds.bst import BST


def build(values):
    t = BST()
    for v in values:
        t.insert(v)
    return t


def test_in_order_is_sorted():
    t = build([5, 3, 8, 1, 4, 7])
    assert t.in_order() == [1, 3, 4, 5, 7, 8]


def test_contains():
    t = build([5, 3, 8])
    assert t.contains(8) is True
    assert t.contains(99) is False


def test_no_duplicates():
    t = build([5, 5, 5])
    assert t.in_order() == [5]
