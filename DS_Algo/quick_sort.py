# coding:utf-8
# example 17: quick_sort.py

import random


# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     pivot_idx = 0
#     pivot = array[pivot_idx]
#     less_part = [num for num in array[pivot_idx + 1:] if num <= pivot]
#     great_part = [num for num in array[pivot_idx + 1:] if num > pivot]
#     return quick_sort(less_part) + [pivot] + quick_sort(great_part)


# def test_quick_sort():
#     import random
#     array = [random.randint(1, 100) for _ in range(10)]
#     sorted_array = sorted(array)
#     my_sorted_array = quick_sort(array)
#     assert my_sorted_array == sorted_array


def partition(array, start, stop):  # [start, stop)
    pivot_idx = start
    pivot = array[pivot_idx]
    left = pivot_idx + 1
    right = stop - 1

    while left <= right:
        while left <= right and array[left] < pivot:
            left += 1
        while left <= right and pivot <= array[right]:
            right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]
    array[pivot_idx], array[right] = array[right], array[pivot_idx]
    return right


def test_partition():
    lst = [3, 1, 4, 2]
    assert partition(lst, 0, len(lst)) == 2

    lst = [1, 2, 3, 4]
    assert partition(lst, 0, len(lst)) == 0

    lst = [4, 3, 2, 1]
    assert partition(lst, 0, len(lst)) == 3

    lst = [3, 5, 4, 3, 6, 7, 2, 3]
    assert partition(lst, 0, len(lst)) == 1


def quick_sort_inplace(array, start, stop):  # [start, stop)
    if start < stop:
        pivot = partition(array, start, stop)
        quick_sort_inplace(array, start, pivot)
        quick_sort_inplace(array, pivot + 1, stop)


def test_quick_sort_inplace():
    seq = [random.randint(-100, 100) for _ in range(10)]
    sorted_seq = sorted(seq)
    quick_sort_inplace(seq, 0, len(seq))
    assert seq == sorted_seq
