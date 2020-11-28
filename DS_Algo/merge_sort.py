# coding:utf-8
# example 16: merge_sort.py

import random


def merge_sort(seq):
    if len(seq) <= 1:
        return seq

    mid = len(seq) // 2
    left_half = merge_sort(seq[:mid])
    right_half = merge_sort(seq[mid:])

    # merge left and right
    new_seq = merge_sorted_list(left_half, right_half)
    return new_seq


def merge_sorted_list(sorted_a, sorted_b):
    len_a, len_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_sorted_seq = list()

    while a < len_a and b < len_b:
        if sorted_a[a] <= sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1
    if a < len_a:
        new_sorted_seq += sorted_a[a:]
    if b < len_b:
        new_sorted_seq += sorted_b[b:]
    return new_sorted_seq


def test_merge_sort():
    seq = [random.randint(-100, 100) for _ in range(10)]
    sorted_seq = sorted(seq)
    my_sorted_seq = merge_sort(seq)
    assert my_sorted_seq == sorted_seq
