# coding:utf-8
# example 05: cyclic_double_linked_list.py

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
            raise Exception("pop form empyt Cyclic Double Linked List")
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
            raise Exception("pop form empyt Cyclic Double Linked List")
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


# use pytest
cdll = CyclicDoubleLinkedList()


class TestDoubleLinkedList(object):

    def test_append(self):
        cdll.append(1)
        cdll.append(2)
        cdll.append(3)
        assert [node.val for node in cdll.iter_node()] == [1, 2, 3]
        assert [node.val for node in cdll.iter_node_reverse()] == [3, 2, 1]

    def test_appendleft(self):
        cdll.appendleft(0)
        assert list(cdll) == [0, 1, 2, 3]

    def test_cyclic(self):
        headnode = cdll.headnode()
        tailnode = cdll.tailnode()
        assert headnode.prev.prev == tailnode
        assert tailnode.next.next == headnode

    def test_len(self):
        assert len(cdll) == 4

    def test_pop(self):
        tail_val = cdll.pop()
        assert tail_val == 3

    def test_popleft(self):
        head_val = cdll.popleft()
        assert head_val == 0

    def test_find(self):
        assert cdll.find(2) == 1
        assert cdll.find(4) == -1

    def test_insert(self):
        cdll.insert(1, 5)
        assert [node.val for node in cdll.iter_node()] == [1, 5, 2]

    def test_remove(self):
        headnode = cdll.root.next
        node = cdll.remove(headnode)
        assert node.val == 1
        assert [node.val for node in cdll.iter_node()] == [5, 2]

    def test_clear_and_empty(self):
        cdll.clear()
        assert cdll.empty() is True
