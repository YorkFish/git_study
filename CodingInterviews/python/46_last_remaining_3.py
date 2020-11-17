#!/usr/bin/env python3
# coding:utf-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1:
            return -1
        dummy = ListNode(0)
        tail = dummy
        for i in range(n):
            node = ListNode(i)
            tail.next = node
            tail = node
        tail.next = dummy.next
        return self.lastRemaining(dummy.next, tail, m)
        
    def lastRemaining(self, head, tail, m):
        cur = head
        pre = tail
        while cur.next is not cur:
            for i in range(m - 1):
                pre = pre.next
                cur = cur.next
            pre.next = cur.next
            cur = cur.next
        return cur.val


if __name__ == "__main__":
    n = 10
    m = 6

    s = Solution()
    ans = s.LastRemaining_Solution(n, m)
    print(ans)
