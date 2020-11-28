# coding:utf-8
# example 18: heap_test.py

import random


class Array(object):
    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, idx):
        return self._items[idx]

    def __setitem__(self, idx, val):
        self._items[idx] = val

    def __len__(self):
        return self._size

    def __iter__(self):
        for item in self._items:
            yield item

    def clear(self, val=None):
        for i in range(len(self._items)):
            self._items[i] = val


# 上面是 Array 的代码，下边是 MaxHeap 的实现
class MaxHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._cnt = 0

    def __len__(self):
        return self._cnt

    def _siftup(self, idx):  # 递归版
        if idx > 0:
            parent = (idx - 1) // 2
            if self._elements[parent] < self._elements[idx]:
                self._elements[parent], self._elements[idx] =\
                    self._elements[idx], self._elements[parent]
                self._siftup(parent)

    def _siftdown(self, idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if right < self._cnt:
            if self._elements[left] < self._elements[right] and\
                    self._elements[largest] < self._elements[right]:
                largest = right
            elif self._elements[largest] < self._elements[left]:
                largest = left
        elif left < self._cnt:
            if self._elements[largest] < self._elements[left]:
                largest = left
        if largest != idx:
            self._elements[largest], self._elements[idx] =\
                    self._elements[idx], self._elements[largest]
            self._siftdown(largest)

    def add(self, val):
        if self._cnt == self.maxsize:
            raise Exception("maxheap full")
        self._elements[self._cnt] = val
        self._siftup(self._cnt)
        self._cnt += 1

    def extract(self):
        if self._cnt == 0:
            raise Exception("maxheap empty")
        val = self._elements[0]
        self._cnt -= 1
        self._elements[0] = self._elements[self._cnt]
        self._siftdown(0)
        return val


def heapsort_reverse(array):
    size = len(array)
    maxheap = MaxHeap(size)
    for num in array:
        maxheap.add(num)
    res = []
    for num in range(size):
        res.append(maxheap.extract())
    return res


# use pytest
size = 5
h = MaxHeap(size)


class TestMaxHeap(object):

    def test_add(self):
        for num in range(size):
            h.add(num)

    def test_extract(self):
        for num in reversed(range(size)):
            assert num == h.extract()

    def test_heapsort_reverse(self):
        seq = [random.randint(-100, 100) for _ in range(10)]
        sorted_seq = sorted(seq, reverse=True)
        heapsorted_seq = heapsort_reverse(seq)
        assert heapsorted_seq == sorted_seq
