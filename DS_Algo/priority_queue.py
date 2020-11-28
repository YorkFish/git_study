# coding:utf-8
# example 19: priority_queue.py


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


# 上边是 Array 的代码，下边是 MaxHeap 的实现
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


# 上边是 MaxHeap 的代码，下边是 PriorityQueue 的实现
class PriorityQueue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._maxheap = MaxHeap(maxsize)

    def push(self, priority, val):
        entry = (priority, val)
        self._maxheap.add(entry)  # 比较的是 priority

    def pop(self, with_priority=False):
        entry = self._maxheap.extract()
        return entry if with_priority else entry[1]

    def empty(self):
        return len(self._maxheap) == 0


# use pytest
size = 5
pq = PriorityQueue(size)


class TestPriorityQueue(object):

    def test_push(self):
        pq.push(5, "神")
        pq.push(3, "鬼")
        pq.push(4, "龙")
        pq.push(1, "狼")
        pq.push(2, "虎")

    def test_pop(self):
        res = []
        while not pq.empty():
            res.append(pq.pop())
        assert res == ["神", "龙", "鬼", "虎", "狼"]
