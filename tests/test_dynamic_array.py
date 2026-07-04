from ds.dynamic_array import DynamicArray


def test_append_and_get():
    arr = DynamicArray()
    arr.append(10)
    arr.append(20)
    assert len(arr) == 2
    assert arr.get(0) == 10
    assert arr.get(1) == 20


def test_grows_past_capacity():
    arr = DynamicArray()
    for i in range(100):
        arr.append(i)
    assert len(arr) == 100
    assert arr.get(99) == 99


def test_out_of_range():
    arr = DynamicArray()
    try:
        arr.get(0)
        assert False, "expected IndexError"
    except IndexError:
        pass
