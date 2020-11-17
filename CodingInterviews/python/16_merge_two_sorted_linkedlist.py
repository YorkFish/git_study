#!/usr/bin/env python3
# coding:utf-8

from helper import ListNode
from helper import print_linked_list


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None: return pHead2
        if pHead2 is None: return pHead1
        
        dummy = ListNode(0)
        cur = dummy
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        if pHead1: cur.next = pHead1
        if pHead2: cur.next = pHead2
        return dummy.next


if __name__ == "__main__":
    a1 = ListNode(1)
    a2 = ListNode(3)
    a3 = ListNode(5)
    a1.next = a2
    a2.next = a3

    b1 = ListNode(2)
    b2 = ListNode(4)
    b3 = ListNode(6)
    b1.next = b2
    b2.next = b3

    s = Solution()
    ans = s.Merge(a1, b1)
    print_linked_list(ans)
