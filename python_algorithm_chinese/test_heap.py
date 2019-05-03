from heap import MaxHeap


def test_max_heap():
    import random
    n = 5
    h = MaxHeap(n)
    for i in random.shuffle(range(n)):
        h.add(i)
    for i in reversed(range(n)):
        assert i == h.extract()
