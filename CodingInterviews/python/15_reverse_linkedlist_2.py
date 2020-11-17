#!/usr/bin/env python3
# coding:utf-8

from helper import ListNode
from helper import print_linked_list


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead

        newHead = self.ReverseList(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return newHead


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    s = Solution()
    ans = s.ReverseList(n1)
    print_linked_list(ans)