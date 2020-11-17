#!/usr/bin/env python3
# coding:utf-8

from helper import RandomListNode
from helper import print_random_linked_list


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead is None:
            return None
        
        # 1->2->3->N => 1->1->2->2->3->3->N
        cur = pHead
        while cur:
            node = RandomListNode(cur.label)
            node.next = cur.next
            cur.next = node
            cur = node.next
        
        # copy random point
        cur = pHead
        while cur:
            if cur.random:
                cur.next.random = cur.random.next  # cur.next 与 cur.random.next 都是 copy node
            cur = cur.next.next
        
        # 1->1->2->2->3->3->N => 1->2->3->N
        cur = pHead
        res = pHead.next
        tmp = pHead.next
        while cur:
            cur.next = cur.next.next
            if tmp.next:
                tmp.next = tmp.next.next
                tmp = tmp.next
            cur = cur.next
        return res


if __name__ == "__main__":
    n1 = RandomListNode(1)
    n2 = RandomListNode(2)
    n3 = RandomListNode(3)
    n4 = RandomListNode(4)
    n5 = RandomListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n1.random = n3
    n2.random = n1
    n3.random = n2
    n4.random = n1
    n5.random = n3
    print_random_linked_list(n1)

    s = Solution()
    new_head = s.Clone(n1)
    print_random_linked_list(new_head)
