from array_and_list import Array

def test_array():
    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1

    a.clear()
    assert a[0] is None