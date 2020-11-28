# coding:utf-8
# example 01: array_test.py

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


def test_array():
    print("pytest -sv array_test.py")

    a = Array(10)

    a[0] = 1
    assert a[0] == 1

    a.clear()
    assert a[0] is None
