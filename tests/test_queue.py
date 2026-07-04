from ds.queue import Queue


def test_fifo_order():
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    assert q.dequeue() == "a"     # first in, first out
    assert q.dequeue() == "b"
    assert q.dequeue() == "c"


def test_front_does_not_remove():
    q = Queue()
    q.enqueue(42)
    assert q.front() == 42
    assert len(q) == 1


def test_dequeue_empty_raises():
    q = Queue()
    try:
        q.dequeue()
        assert False, "expected IndexError"
    except IndexError:
        pass
