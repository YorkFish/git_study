#!/usr/bin/env python3
# coding:utf-8

from helper import ListNode


class Solution:
    def __init__(self):
        self.stk = []
        self.cache = []

    def push(self, node):
        self.stk.append(node)

    def pop(self):
        while self.stk:
            self.cache.append(self.stk.pop())

        res = None
        if self.cache != []:
            res = self.cache.pop()
            while self.cache:
                self.stk.append(self.cache.pop())
        return res


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    s = Solution()
    s.push(n1)
    s.push(n2)
    print(s.pop().val)
    s.push(n3)
    s.push(n4)
    print(s.pop().val)
