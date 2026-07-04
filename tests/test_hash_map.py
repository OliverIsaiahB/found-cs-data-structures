from ds.hash_map import HashMap
import pytest


def test_put_and_get():
    m = HashMap()
    m.put("a", 1)
    m.put("b", 2)
    assert m.get("a") == 1
    assert m.get("b") == 2


def test_update_existing_key():
    m = HashMap()
    m.put("x", 1)
    m.put("x", 99)        # same key → overwrite, not duplicate
    assert m.get("x") == 99
    assert len(m) == 1


def test_missing_key_raises():
    m = HashMap()
    with pytest.raises(KeyError):
        m.get("nope")


def test_many_keys_after_resize():
    m = HashMap()
    for i in range(50):
        m.put(i, i * i)
    assert len(m) == 50
    assert m.get(49) == 49 * 49
