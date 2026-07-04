from ds.doubly_linked_list import DoublyLinkedList


def test_append_tail_order():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    assert dll.to_list_forward() == [1, 2, 3]   # appended at the tail, in order
    assert len(dll) == 3


def test_prepend_head_order():
    dll = DoublyLinkedList()
    dll.prepend(1)
    dll.prepend(2)
    assert dll.to_list_forward() == [2, 1]


def test_backward_traversal():
    dll = DoublyLinkedList()
    dll.append("a")
    dll.append("b")
    dll.append("c")
    assert dll.to_list_backward() == ["c", "b", "a"]
