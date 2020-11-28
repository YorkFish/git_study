# coding:utf-8
# example 07: array_queue.py

import pytest


class Array(object):
    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, val):
        self._items[index] = val

    def __len__(self):
        return self._size

    def clear(self, val=None):
        for i in range(len(self._items)):
            self._items[i] = val

    def __iter__(self):
        for item in self._items:
            yield item


# 上面是 Array 的代码，下边是 ArrayQueue 的实现
class EmptyError(Exception):
    pass


class FullError(Exception):
    pass


class ArrayQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0  # 模拟队头
        self.tail = 0  # 模拟队尾

    def __len__(self):
        return self.tail - self.head

    def push(self, val):
        if len(self) == self.maxsize:
            raise FullError("array queue full")
        self.array[self.tail % self.maxsize] = val
        self.tail += 1

    def pop(self):
        if self.tail ==self.head:
            raise EmptyError("pop from empty array queue")
        val = self.array[self.head % self.maxsize]
        self.head += 1
        return val


# use pytest
size = 5
q = ArrayQueue(size)


class TestQueue(object):

    def test_push(self):
        for i in range(size):
            q.push(i)

    def test_len(self):
        assert len(q) == 5

    def test_full_error(self):
        with pytest.raises(FullError) as excinfo:
            q.push(6)
        assert "array queue full" == str(excinfo.value)

    def test_pop(self):
        assert q.pop() == 0
        assert q.pop() == 1

    def test_push_again(self):
        q.push(5)
        assert len(q) == 4

    def test_pop_all(self):
        assert q.pop() == 2
        assert q.pop() == 3
        assert q.pop() == 4
        assert q.pop() == 5
        assert len(q) == 0

    def test_empty_error(self):
        with pytest.raises(EmptyError) as excinfo:
            q.pop()
        assert "pop from empty array queue" == str(excinfo.value)
