# coding:utf-8
# example 09: stack_test.py

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
class Deque(CyclicDoubleLinkedList):

    def pop(self):
        if len(self) == 0:
            raise Exception("empty")
        tailnode = self.tailnode()
        val = tailnode.val
        self.remove(tailnode)
        return val

    def popleft(self):
        if len(self) == 0:
            raise Exception("empty")
        headnode = self.headnode()
        val = headnode.val
        self.remove(headnode)
        return val


# 下边是 Stack 的实现
class Stack(object):
    def __init__(self):
        self.deque = Deque()

    def __len__(self):
        return len(self.deque)

    def empty(self):
        return len(self) == 0

    def peek(self):
        if not self.empty():
            return self.deque.tailnode().val

    def push(self, val):
        return self.deque.append(val)

    def pop(self):
        return self.deque.pop()


# use pytest
s = Stack()


class TestStack(object):

    def test_push(self):
        for i in range(3):
            s.push(i)

    def test_len(self):
        assert len(s) == 3

    def test_peek(self):
        assert s.peek() == 2

    def test_pop(self):
        assert s.pop() == 2
        assert s.pop() == 1
        assert s.pop() == 0

    def test_empty(self):
        assert s.empty() is True

    def test_empty_error(self):
        with pytest.raises(Exception) as excinfo:
            s.pop()
        assert "empty" == str(excinfo.value)
