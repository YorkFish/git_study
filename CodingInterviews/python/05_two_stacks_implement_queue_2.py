#!/usr/bin/env python3
# coding:utf-8

from helper import ListNode


class Solution:
    def __init__(self):
        self.acceptStack = []
        self.outputStack = []

    def push(self, node):
        self.acceptStack.append(node)

    def pop(self):
        if self.outputStack == []:
            while self.acceptStack:
                self.outputStack.append(self.acceptStack.pop())

        if self.outputStack != []:
            return self.outputStack.pop()
        else:
            return None


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
