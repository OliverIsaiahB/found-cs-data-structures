from ds.linked_list import LinkedList


def test_prepend_order():
    ll = LinkedList()
    ll.prepend(1)
    ll.prepend(2)
    ll.prepend(3)
    assert ll.to_list() == [3, 2, 1]   # newest at the front
    assert len(ll) == 3


def test_get_by_index():
    ll = LinkedList()
    ll.prepend("c")
    ll.prepend("b")
    ll.prepend("a")
    assert ll.get(0) == "a"
    assert ll.get(2) == "c"


def test_get_out_of_range():
    ll = LinkedList()
    try:
        ll.get(0)
        assert False, "expected IndexError"
    except IndexError:
        pass
