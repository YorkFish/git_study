# coding:utf-8
# example 14: select_sort.py

import random


def select_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        if min_idx != i:
            seq[min_idx], seq[i] = seq[i], seq[min_idx]


def test_select_sort():
    seq = [random.randint(-100, 100) for i in range(10)]
    sorted_seq = sorted(seq)
    select_sort(seq)
    assert seq == sorted_seq
