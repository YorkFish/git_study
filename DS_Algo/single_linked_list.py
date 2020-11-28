# coding:utf-8
# example 02: single_linked_list.py

class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SingleLinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize  # None 表示不限大小；数字表示上限大小
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
        if self.root.next is None:
            raise Exception("pop from empty Single Linked List")
        val = self.tailnode.val
        tailnode = self.root
        for _ in range(self.length - 1):
            tailnode = tailnode.next
        tailnode.next = None
        del self.tailnode
        self.length -= 1
        self.tailnode = None if tailnode is self.root else tailnode
        return val

    def popleft(self):  # O(1)
        if self.root.next is None:
            raise Exception("pop from empty Single Linked List")
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
        """
        return 1: 删除成功
        return -1: 删除失败
        """
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


# use pytest
sll = SingleLinkedList()


class TestSingleLinkedList(object):
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_append(self):
        sll.append(1)
        sll.append(2)
        sll.append(3)
        assert list(sll) == [1, 2, 3]

    def test_appendleft(self):
        sll.appendleft(0)
        assert list(sll) == [0, 1, 2, 3]

    def test_len(self):
        assert len(sll) == 4

    def test_pop(self):
        tail_val = sll.pop()
        assert tail_val == 3

    def test_popleft(self):
        head_val = sll.popleft()
        assert head_val == 0

    def test_find(self):
        assert sll.find(2) == 1
        assert sll.find(4) == -1

    def test_insert(self):
        sll.insert(1, 5)
        assert list(sll) == [1, 5, 2]

    def test_remove(self):
        sll.remove(5)
        assert list(sll) == [1, 2]

    def test_clear_and_empty(self):
        sll.clear()
        assert sll.empty() is True
