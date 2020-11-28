# coding:utf-8
# example 13: bubble_sort.py

import random


def bubble_sort1(seq):
    """升序，从左向右定序"""
    n = len(seq)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if seq[j] < seq[i]:
                seq[j], seq[i] = seq[i], seq[j]


def bubble_sort2(seq):
    """升序，从右向左定序"""
    n = len(seq)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if seq[j + 1] < seq[j]:
                seq[j + 1], seq[j] = seq[j], seq[j + 1]


def test_bubble_sort1():
    seq = [random.randint(-100, 100) for i in range(10)]
    sorted_seq = sorted(seq)
    bubble_sort1(seq)
    assert seq == sorted_seq


def test_bubble_sort2():
    seq = [random.randint(-100, 100) for i in range(10)]
    sorted_seq = sorted(seq)
    bubble_sort2(seq)
    assert seq == sorted_seq
