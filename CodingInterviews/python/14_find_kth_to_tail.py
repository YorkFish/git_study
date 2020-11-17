#!/usr/bin/env python3
# coding:utf-8

from helper import ListNode


class Solution:
    def FindKthToTail(self, head, k):
        first = head
        for _ in range(k):
            if first is None:
                return None
            first = first.next
        second = head
        while first:
            first = first.next
            second = second.next
        return second


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    s = Solution()
    print(s.FindKthToTail(n1, 5).val)