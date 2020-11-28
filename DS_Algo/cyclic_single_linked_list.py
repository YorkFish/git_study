# coding:utf-8
# example 03: cyclic_single_linked_list.py

class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


class CyclicSingleLinkedList(object):
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
        node.next = self.root.next
        self.tailnode = node
        self.length += 1

    def appendleft(self, val):  # O(1)
        node = Node(val)
        node.next = self.root.next
        self.root.next = node
        self.length += 1
        if self.length == 1:
            node.next = node
            self.tailnode = node
        else:
            self.tailnode.next = node

    def pop(self):  # O(n)
        if self.length == 0:
            raise Exception("pop from empty Single Linked List")
        val = self.tailnode.val
        if self.length == 1:
            self.root.next = None
            del self.tailnode
            self.tailnode = None
        else:
            tailnode = self.root
            for _ in range(self.length - 1):
                tailnode = tailnode.next
            tailnode.next = self.root.next
            del self.tailnode
            self.tailnode = tailnode
        self.length -= 1
        return val

    def popleft(self):  # O(1)
        if self.length == 0:
            raise Exception("pop from empty Single Linked List")
        headnode = self.root.next
        val = headnode.val
        if self.length == 1:
            self.root.next = None
            self.tailnode = None
        else:
            self.root.next = headnode.next
            self.tailnode.next = headnode.next
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
        """
        return 1: 删除成功
        return -1: 删除失败
        """
        if self.length == 0:
            return -1
        if self.length == 1:
            headnode = self.root.next
            if headnode.val == val:
                self.root.next = None
                self.tailnode = None
                del headnode
                self.length -= 1
                return 1
            else:
                return -1
        pre = self.root
        for cur in self.iter_node():
            if cur.val == val:
                headnode = self.root.next
                if cur is headnode:
                    self.root.next = headnode.next
                    self.tailnode.next = headnode.next
                elif cur is self.tailnode:
                    self.tailnode = pre
                    self.tailnode.next = headnode
                else:
                    pre.next = cur.next
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


# use pytest
csll = CyclicSingleLinkedList()


class TestCyclicSingleLinkedList(object):

    def test_append(self):
        csll.append(1)
        csll.append(2)
        csll.append(3)
        assert list(csll) == [1, 2, 3]

    def test_appendleft(self):
        csll.appendleft(0)
        assert list(csll) == [0, 1, 2, 3]

    def test_cyclic(self):
        headnode = csll.root.next
        assert csll.tailnode.next is headnode

    def test_len(self):
        assert len(csll) == 4

    def test_pop(self):
        tail_val = csll.pop()
        assert tail_val == 3

    def test_popleft(self):
        head_val = csll.popleft()
        assert head_val == 0

    def test_find(self):
        assert csll.find(2) == 1
        assert csll.find(4) == -1

    def test_insert(self):
        csll.insert(1, 5)
        assert list(csll) == [1, 5, 2]

    def test_remove(self):
        csll.remove(1)
        csll.remove(2)
        assert list(csll) == [5]

    def test_clear_and_empty(self):
        csll.clear()
        assert csll.empty() is True
