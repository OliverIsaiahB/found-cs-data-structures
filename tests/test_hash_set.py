from ds.hash_set import HashSet


def test_add_and_contains():
    s = HashSet()
    s.add(1)
    s.add(2)
    assert s.contains(1)
    assert s.contains(2)
    assert not s.contains(3)


def test_no_duplicates():
    s = HashSet()
    s.add("x")
    s.add("x")
    s.add("x")
    assert len(s) == 1          # added once, no matter how many times


def test_union():
    a = HashSet()
    a.add(1); a.add(2)
    b = HashSet()
    b.add(2); b.add(3)
    u = a.union(b)
    assert len(u) == 3          # {1, 2, 3} — the shared 2 isn't double-counted
    assert u.contains(1) and u.contains(2) and u.contains(3)
