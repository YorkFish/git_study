#!/usr/bin/env python3
# coding:utf-8

"""
BinaryTreeTraverse
ListNode
PrintTree
RandomListNode
TreeLinkNode
TreeNode

bubble
fibonacci
print_deque
print_linked_list
print_random_linked_list
"""


# class
class BinaryTreeTraverse(object):
    def pre_order(self, root):
        if root is None:
            return None

        print(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)

    def mid_order(self, root):
        if root is None:
            return None

        self.mid_order(root.left)
        print(root.val)
        self.mid_order(root.right)

    def lat_order(self, root):
        if root is None:
            return None

        self.lat_order(root.left)
        self.lat_order(root.right)
        print(root.val)


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class PrintTree(object):
    def from_top_to_bottom(self, root):
        if root is None:
            print("the root is None")
            return

        queue = [root]
        res = []
        while queue != []:
            node = queue.pop(0)
            res.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        for num in res:
            print(num, end=' ')
        print()


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# def
def bubble(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j+1] < array[j]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def create_linked_list(lst):
    p = head = ListNode(lst[0])
    n = len(lst)
    for i in range(1, n):
        p.next = ListNode(lst[i])
        p = p.next
    return head


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def print_deque(left_node, right_node):
    if left_node is None and right_node is None:
        print("can not print deque")
        return None

    print("from left to right:", end=' ')
    while left_node:
        print(left_node.val, end=' ')
        left_node = left_node.right
    print()

    print("from right to left:", end=' ')
    while right_node:
        print(right_node.val, end=' ')
        right_node = right_node.left
    print()


def print_linked_list(p_head):
    if p_head is None:
        print("None")
        return None

    while p_head is not None:
        print(p_head.val, end=" -> ")
        p_head = p_head.next
    print("None")


def print_random_linked_list(p_head):
    if p_head is None:
        return None

    cur = p_head
    while cur is not None:
        print(cur.label, end=" -> ")
        cur = cur.next
    print("None")

    cur = p_head
    while cur is not None:
        print(f"{cur.label}.random = {cur.random.label}")
        cur = cur.next
