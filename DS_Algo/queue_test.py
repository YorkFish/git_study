# coding:utf-8
# example 06: queue_test.py

import pytest


class Node(object):
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt


class SingleLinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def iter_node(self):
        cur = self.root
        for _ in range(self.length):
            cur = cur.next
            yield cur

    def __iter__(self):
        for node in self.iter_node():
            yield node.val

    def empty(self):
        return self.length == 0

    def append(self, val):  # O(1)
        if self.maxsize is not None and self.length == self.maxsize:
            raise Exception("Full")
        node = Node(val)
        if self.tailnode is None:
            self.root.next = node
        else:
            self.tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, val):  # O(1)
        node = Node(val)
        node.next = self.root.next
        self.root.next = node
        self.length += 1
        if self.length == 1:
            self.tailnode = node

    def pop(self):  # O(n)
        if self.length == 0:
            raise Exception("pop from empty Single Linked List")
        val = self.tailnode.val
        tailnode = self.root
        for _ in range(self.length - 1):
            tailnode = tailnode.next
        tailnode.next = None
        del self.tailnode
        self.length -= 1
        self.tailnode = None if self.length == 0 else tailnode
        return val

    def popleft(self):  # O(1)
        if self.length == 0:
            raise Exception("pop from empty LinkedList")
        headnode = self.root.next
        val = headnode.val
        self.root.next = headnode.next
        if headnode is self.tailnode:
            self.tailnode = None
        del headnode
        self.length -= 1
        return val

    def find(self, val):  # O(n)
        for idx, node in enumerate(self.iter_node()):
            if node.val == val:
                return idx
        return -1

    def insert(self, pos, val):  # O(n)
        if pos <= 0:
            self.appendleft(val)
        elif self.length - 1 < pos:
            self.append(val)
        else:
            node = Node(val)
            pre = self.root
            for _ in range(pos):
                pre = pre.next
            node.next = pre.next
            pre.next = node
            self.length += 1

    def remove(self, val):  # O(n)
        if self.length == 0:
            return -1
        pre = self.root
        for cur in self.iter_node():
            if cur.val == val:
                pre.next = cur.next
                if cur is self.tailnode:
                    self.tailnode = None if self.length == 1 else pre
                del cur
                self.length -= 1
                return 1
            pre = pre.next
        return -1

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.tailnode = None
        self.length = 0


# 上面是 SingleLinkedList 的代码，下边是 Queue 的实现
class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class Queue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_linkedlist = SingleLinkedList()

    def __len__(self):
        return len(self._item_linkedlist)

    def push(self, val):
        if self.maxsize is not None and len(self) == self.maxsize:
            raise FullError("queue full")
        self._item_linkedlist.append(val)

    def pop(self):
        if len(self) == 0:
            raise EmptyError("queue empty")
        return self._item_linkedlist.popleft()


# use pytest
q = Queue()


class TestQueue(object):

    def test_push(self):
        q.push(0)
        q.push(1)
        q.push(2)
        assert len(q) == 3

    def test_pop(self):
        assert q.pop() == 0
        assert q.pop() == 1
        assert q.pop() == 2

    def test_empty_error(self):
        with pytest.raises(EmptyError) as excinfo:
            q.pop()  # raise EmptyError
        assert "queue empty" == str(excinfo.value)
