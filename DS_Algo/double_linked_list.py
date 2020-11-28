# coding:utf-8
# example 04: double_linked_list.py

class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def iter_node(self):
        if self.length == 0:
            return
        cur = self.root
        for _ in range(self.length):
            cur = cur.next
            yield cur

    def __iter__(self):
        for node in self.iter_node():
            yield node.val

    def iter_node_reverse(self):
        if self.length == 0:
            return
        cur = self.tailnode
        for _ in range(self.length):
            yield cur
            cur = cur.prev

    def empty(self):
        return self.root.next is None

    def append(self, val):  # O(1)
        if self.maxsize is not None and self.length == self.maxsize:
            raise Exception("Full")
        node = Node(val)
        if self.length == 0:
            node.prev = self.root
            self.root.next = node
        else:
            node.prev = self.tailnode
            self.tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, val):  # O(1)
        if self.maxsize is not None and self.length == self.maxsize:
            raise Exception("Full")
        node = Node(val)
        if self.length == 0:
            node.prev = self.root
            self.root.next = node
            self.tailnode = node
        else:
            node.prev = self.root
            node.next = self.root.next
            self.root.next.prev = node
            self.root.next = node
        self.length += 1

    def pop(self):  # O(1)
        if self.length == 0:
            raise Exception("pop form empty Double Linked List")
        val = self.tailnode.val
        tailnode = self.tailnode.prev
        tailnode.next = None
        del self.tailnode
        self.length -= 1
        self.tailnode = None if self.length == 0 else tailnode
        return val

    def popleft(self):  # O(1)
        if self.length == 0:
            raise Exception("pop form empty Double Linked List")
        headnode = self.root.next
        val = headnode.val
        self.root.next = headnode.next
        if headnode is self.tailnode:
            self.tailnode = None
        else:
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
        if self.length == 0:
            return
        if self.length == 1:
            self.root.next = None
            self.tailnode = None
        elif node is self.tailnode:
            self.tailnode = node.prev
            self.tailnode.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.tailnode = None
        self.length = 0


# use pytest
dll = DoubleLinkedList()


class TestDoubleLinkedList(object):

    def test_append(self):
        dll.append(1)
        dll.append(2)
        dll.append(3)
        assert [node.val for node in dll.iter_node()] == [1, 2, 3]
        assert [node.val for node in dll.iter_node_reverse()] == [3, 2, 1]

    def test_appendleft(self):
        dll.appendleft(0)
        assert list(dll) == [0, 1, 2, 3]

    def test_len(self):
        assert len(dll) == 4

    def test_pop(self):
        tail_val = dll.pop()
        assert tail_val == 3

    def test_popleft(self):
        head_val = dll.popleft()
        assert head_val == 0

    def test_find(self):
        assert dll.find(2) == 1
        assert dll.find(4) == -1

    def test_insert(self):
        dll.insert(1, 5)
        assert [node.val for node in dll.iter_node()] == [1, 5, 2]

    def test_remove(self):
        headnode = dll.root.next
        node = dll.remove(headnode)
        assert node.val == 1
        assert [node.val for node in dll.iter_node()] == [5, 2]

    def test_clear_and_empty(self):
        dll.clear()
        assert dll.empty() is True
