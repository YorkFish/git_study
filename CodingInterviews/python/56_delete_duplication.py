#!/usr/bin/env python3
# coding:utf-8

from helper import ListNode
from helper import create_linked_list, print_linked_list

class Solution:
    # 1->2->3->3->4->4->5 => 1->2->5
    def deleteDuplication(self, pHead):
        dummy = ListNode(-1)
        dummy.next = pHead
        pre = dummy
        while pre.next:
            cur = pre.next
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                pre.next = cur.next
            else:
                pre = cur
        return dummy.next


if __name__ == "__main__":
    # 1->2->3->3->4->4->5->None
    h1 = create_linked_list([1, 2, 3, 3, 4, 4, 5])

    # 2->2->3->None
    h2 = create_linked_list([2, 2, 3])

    # 1->1->1->1->1->1->1->None
    h3 = create_linked_list([1, 1, 1, 1, 1, 1, 1])

    pHead = h3
    s = Solution()
    print_linked_list(pHead)
    ans = s.deleteDuplication(pHead)
    print_linked_list(ans)
