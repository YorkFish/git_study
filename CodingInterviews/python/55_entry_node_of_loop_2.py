#!/usr/bin/env python3
# coding:utf-8

"""
         <- o <-
     b  /       \
        o        o
     s   \      /  a
o -> o -> o -> o

2 * (s + a) = s + n * (a + b) + a

=> s = n (a + b) - a = (n - 1) * a + n * b = (n - 1) * (a + b) + b

=> {s -> cross} = {b -> corss}
"""

from helper import ListNode


class Solution:
    def EntryNodeOfLoop(self, pHead):
        slow = fast = pHead
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            if fast and fast is slow:
                fast = pHead
                while fast is not slow:
                    fast = fast.next
                    slow = slow.next
                break
        return fast


if __name__ == "__main__":
    """
              8 <- 7 <- 6
              v         ^
    1 -> 2 -> 3 -> 4 -> 5
    """
    head = tail = ListNode(1)
    for i in range(2, 9):
        tail.next = ListNode(i)
        tail = tail.next
        if i == 3:
            corss = tail
    tail.next = corss

    s = Solution()
    ans = s.EntryNodeOfLoop(head)
    if ans:
        print(ans.val)
    else:
        print(ans)
