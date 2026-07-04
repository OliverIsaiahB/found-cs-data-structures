from ds.min_heap import MinHeap


def test_pops_in_sorted_order():
    h = MinHeap()
    for v in [5, 1, 8, 3, 2]:
        h.push(v)
    out = [h.pop_min() for _ in range(5)]
    assert out == [1, 2, 3, 5, 8]      # smallest first, every time


def test_peek_min():
    h = MinHeap()
    h.push(10)
    h.push(4)
    assert h.peek_min() == 4
    assert len(h) == 2                  # peek does not remove


def test_pop_empty_raises():
    h = MinHeap()
    try:
        h.pop_min()
        assert False, "expected IndexError"
    except IndexError:
        pass
