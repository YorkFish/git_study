# coding:utf-8
# example 18: quick_sort.py

import random


def shell_sort(seq):
    cnt = 0
    n = len(seq)
    gap = n // 2  # 初始步长
    while gap > 0:
        for i in range(gap, n, gap):  # 按步长进行插入排序
            cnt += 1
            j = i
            while gap <= j and seq[j] < seq[j-gap]:  # 插入排序
                seq[j], seq[j-gap] = seq[j-gap], seq[j]
                j -= gap
        gap //= 2  # 得到新的步长
    return cnt


# use pytest
def test_shell_sort():
    seq = [random.randint(-100, 100) for _ in range(10)]
    sorted_seq = sorted(seq)
    cnt = shell_sort(seq)
    print("cnt =", cnt)
    assert seq == sorted_seq
