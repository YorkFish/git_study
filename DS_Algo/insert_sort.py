# coding:utf-8
# example 15: insert_sort.py

import random


def insert_sort(seq):
    """整理纸牌的感觉"""
    for i in range(1, len(seq)):
        pos, val = i, seq[i]
        while pos > 0 and val < seq[pos - 1]:
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = val


def test_insert_sort():
    seq = [random.randint(-100, 100) for i in range(10)]
    sorted_seq = sorted(seq)
    insert_sort(seq)
    assert seq == sorted_seq
