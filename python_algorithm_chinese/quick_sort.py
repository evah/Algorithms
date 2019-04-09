# -*- coding: utf-8 -*-


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot_index = 0
        pivot = array[pivot_index]
        less_part = [i for i in array[pivot_index + 1:] if i <= pivot]
        great_part = [i for i in array[pivot_index + 1:]if i > pivot]
        return quicksort(less_part) + [pivot] + quicksort(great_part)


def partition(array, beg, end):
    pivot_index = beg
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1

    while True:
        while left <= right and array[left] < pivot:
            left += 1

        while right >= left and array[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]

    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right


def test_partition():
    l = [4, 1, 2, 8]
    assert partition(l, 0, len(l)) == 2
    l = [1, 2, 3, 4]
    assert partition(l, 0, len(l)) == 0
    l = [4, 3, 2, 1]
    assert partition(l, 0, len(l)) == 3


def quicksort_inplace(array, beg, end):
    if beg < end:
        pivot = partition(array, beg, end)
        quicksort_inplace(array, beg, pivot)
        quicksort_inplace(array, pivot + 1, end)


def test_quicksort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    assert quicksort(seq) == sorted_seq


def test_quicksort_inplace():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    quicksort_inplace(seq, 0, len(seq))
    assert seq == sorted_seq


def nth_element(array, beg, end, nth):
    if beg < end:
        pivot_idx = partition(array, beg, end)
        if pivot_idx == nth - 1:
            return array[pivot_idx]
        elif pivot_idx > nth - 1:
            return nth_element(array, beg, pivot_idx, nth)
        else:
            return nth_element(array, pivot_idx + 1, end, nth)


def test_nth_element():
    l1 = [3, 5, 4, 2, 1]
    assert nth_element(l1, 0, len(l1), 3) == 3
    assert nth_element(l1, 0, len(l1), 2) == 2

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in l:
        assert nth_element(l, 0, len(l), i) == i
    for i in reversed(l):
        assert nth_element(l, 0, len(l), i) == i

    array = [3, 2, 1, 5, 6, 4]
    assert nth_element(array, 0, len(array), 2) == 2

    array = [2, 1]
    assert nth_element(array, 0, len(array), 1) == 1
    assert nth_element(array, 0, len(array), 2) == 2

    array = [3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert nth_element(array, 0, len(array), 1) == 3
