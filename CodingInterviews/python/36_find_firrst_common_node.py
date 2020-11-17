#!/usr/bin/env python3
# coding:utf-8

from helper import ListNode


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 is None or pHead2 is None:
            return None

        cur1 = pHead1
        cur2 = pHead2
        while cur1 != cur2:
            if cur1:
                cur1 = cur1.next
            else:
                cur1 = pHead2
            if cur2:
                cur2 = cur2.next
            else:
                cur2 = pHead1
        return cur1


if __name__ == "__main__":
    """
    1->2->3
           \
            4->5->6->None
           /
       7->8
    """
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)
    a6 = ListNode(6)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6

    b1 = ListNode(7)
    b2 = ListNode(8)
    b1.next = b2
    b2.next = a4

    s = Solution()
    ans = s.FindFirstCommonNode(a1, b1)
    if ans is None:
        print("None")
    else:
        print(ans.val)
