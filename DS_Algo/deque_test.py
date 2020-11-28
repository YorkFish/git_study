# coding:utf-8
# example 08: deque_test.py

import pytest


class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None


class CyclicDoubleLinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.prev = node
        node.next = node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def iter_node(self):
        if self.length == 0:
            return
        cur = self.headnode()
        for _ in range(self.length):
            yield cur
            cur = cur.next

    def __iter__(self):
        for node in self.iter_node():
            yield node.val

    def iter_node_reverse(self):
        if self.length == 0:
            return
        cur = self.tailnode()
        for _ in range(self.length):
            yield cur
            cur = cur.prev

    def empty(self):
        return self.root.next is self.root

    def append(self, val):  # O(1)
        if self.maxsize is not None and self.length == self.maxsize:
            raise Exception("Full")
        node = Node(val)
        tailnode = self.tailnode()
        tailnode.next = node
        node.next = self.root
        self.root.prev = node
        node.prev = tailnode
        self.length += 1

    def appendleft(self, val):  # O(1)
        if self.maxsize is not None and self.length == self.maxsize:
            raise Exception("Full")
        node = Node(val)
        if self.length == 0:
            self.root.next = node
            node.next = self.root
            self.root.prev = node
            node.prev = self.root
        else:
            node.prev = self.root
            node.next = self.root.next
            self.root.next.prev = node
            self.root.next = node
        self.length += 1

    def pop(self):  # O(1)
        if self.length == 0:
            raise Exception("pop form empty Cyclic Double Linked List")
        tailnode = self.tailnode()
        val = tailnode.val
        tmp_tailnode = tailnode.prev
        tmp_tailnode.next = self.root
        self.root.prev = tmp_tailnode
        del tailnode
        self.length -= 1
        return val

    def popleft(self):  # O(1)
        if self.length == 0:
            raise Exception("pop form empty Cyclic Double Linked List")
        headnode = self.headnode()
        val = headnode.val
        if self.length == 1:
            self.root.next = self.root
            self.root.prev = self.root
        else:
            self.root.next = headnode.next
            headnode.next.prev = self.root
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
            node.prev = pre
            node.next = pre.next
            node.next.prev = node
            pre.next = node
            self.length += 1

    def remove(self, node):  # O(1), node is not value
        if node is self.root:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1
        return node

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = self.root
        self.root.prev = self.root
        self.length = 0


# 上面是 CyclicDoubleLinkedList 的代码，下边是 Deque 的实现
class EmptyError(Exception):
    pass


class FullError(Exception):
    pass


class Deque(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_deque = CyclicDoubleLinkedList()

    def __len__(self):
        return len(self._item_deque)

    def append(self, val):
        if self.maxsize is not None and len(self) == self.maxsize:
            raise FullError("deque full")
        self._item_deque.append(val)

    def appendleft(self, val):
        if self.maxsize is not None and len(self) == self.maxsize:
            raise FullError("deque full")
        self._item_deque.appendleft(val)

    def pop(self):
        if self._item_deque.empty():
            raise EmptyError("deque empty")
        return self._item_deque.pop()

    def popleft(self):
        if self._item_deque.empty():
            raise EmptyError("deque empty")
        return self._item_deque.popleft()


# use pytest
dq = Deque()


class TestDeque():

    def test_append(self):
        dq.append(2)
        dq.append(3)

    def test_len(self):
        assert len(dq) == 2

    def test_appendleft(self):
        dq.appendleft(1)
        dq.appendleft(0)
        assert len(dq) == 4

    def test_pop(self):
        assert dq.pop() == 3
        assert dq.pop() == 2

    def test_popleft(self):
        assert dq.popleft() == 0
        assert dq.popleft() == 1

    def test_empty_error(self):
        with pytest.raises(EmptyError) as excinfo:
            dq.pop()
        assert "deque empty" == str(excinfo.value)
