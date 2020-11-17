#!/usr/bin/env python3
# coding:utf-8

from helper import ListNode
from helper import print_linked_list


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        
        pre = None
        cur = pHead
        while cur.next:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        cur.next = pre
        return cur


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    s = Solution()
    ans = s.ReverseList(n1)
    print_linked_list(ans)