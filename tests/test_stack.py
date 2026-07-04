from ds.stack import Stack


def test_lifo_order():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3      # last in, first out
    assert s.pop() == 2
    assert s.pop() == 1


def test_peek_does_not_remove():
    s = Stack()
    s.push("a")
    assert s.peek() == "a"
    assert len(s) == 1       # still there


def test_pop_empty_raises():
    s = Stack()
    try:
        s.pop()
        assert False, "expected IndexError"
    except IndexError:
        pass
