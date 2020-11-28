# coding:utf-8
# example 13: recursion.py

from collections import deque


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def print_num_recursive(n):
    if n > 0:
        print_num_recursive(n - 1)
        print(n)


class Stack(object):
    def __init__(self):
        self._deque = deque()

    def push(self, val):
        return self._deque.append(val)

    def pop(self):
        return self._deque.pop()

    def is_empty(self):
        return len(self._deque) == 0


def print_num_use_stack(n):
    s = Stack()
    while n > 0:
        s.push(n)
        n -= 1

    while not s.is_empty():
        print(s.pop())


print_num_use_stack(5)
