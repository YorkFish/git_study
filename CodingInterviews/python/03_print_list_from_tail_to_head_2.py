#!/usr/bin/env python3
# coding:utf-8

from helper import ListNode


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode is None: 
            return [] 
        return self.printListFromTailToHead(listNode.next) + [listNode.val]


if __name__ == "__main__":
    # 1 -> 2 -> 3 -> None
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    s = Solution()
    ans = s.printListFromTailToHead(n1)
    print(ans)
