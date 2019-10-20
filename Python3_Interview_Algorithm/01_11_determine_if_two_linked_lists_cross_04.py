#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

"""
我之前在 Bilibili 上见一个 Up 有另一种思路，和方法三很像，但又不完全相等
简单地说，就是从两个头结点同时出发，速度为 1
    若走到尾部，就跳到另一个链表继续走
    若两个链表相交，就会在交点相遇
    若两个链表不相交，各自的“指针”最后会同时走到另一条链表的 None
视频一时三刻找不到，我按这个思路自己实现一下
"""
def isIntersect(head1, head2):
    """
    方法功能：判断两个链表是否相交；若相交，找出交点
    输入参数：head1 与 head2 分别表示两个链表的头结点
    返回值：若相交，返回相交结点；若不相交，返回 None
    """
    if head1 is None or head1.next is None or head2 is None or head2 is None:
        return None

    cur1 = head1.next
    cur2 = head2.next
    while cur1 and cur2:
        if cur1 is cur2:
            return cur1
        cur1 = cur1.next
        cur2 = cur2.next
        if cur1 is None and cur2 is None:
            return None
        elif cur1 is None:
            cur1 = head2.next
        elif cur2 is None:
            cur2 = head1.next

def constructLinkedList(nums, t):
    """
    方法功能：创建单链表
    输入参数：nums: 作为链表结点的数据；t: 1 表示要 tail，0 表示不要
    返回值：head: 链表头结点；cur: 链表尾结点
    """
    head = LNode()
    cur = head
    for num in nums:
        tmp = LNode()
        tmp.val = num
        cur.next = tmp
        cur = tmp
    if t:
        return head, cur
    return head

def printLinkedList(head):
    """ 打印单链表 """
    print("head->", end='')
    cur = head.next
    while cur:
        print(cur.val, end="->")
        cur = cur.next
    print("None")
    return None

def ans(meet_node):
    if meet_node:
        print(f"\nTwo linked lists cross. The intersection value is {meet_node.val}.")
    else:
        print("\nnon-intersect!")
    return None

if __name__ == "__main__":
    head1, tail1 = constructLinkedList([1, 2, 3, 4], 1)
    head2, tail2 = constructLinkedList([5, 6, 7], 1)
    head3 = constructLinkedList([8, 9, 10], 0)
    tail1.next = head3.next
    tail2.next = head3.next

    print("head1:", end=' ')
    printLinkedList(head1)
    print("\nhead2:", end=' ')
    printLinkedList(head2)
    """
    head1->1->2->3->4
                     \
                      ->8->9->10->None
                    /
    head2->5->6->7-
    """
    head3 = constructLinkedList([11, 12, 13, 14], 0)
    head4 = constructLinkedList([15, 16, 17], 0)
    print("\nhead3:", end=' ')
    printLinkedList(head3)
    print("\nhead4:", end=' ')
    printLinkedList(head4)

    meet_node1 = isIntersect(head1, head2)
    meet_node2 = isIntersect(head3, head4)
    ans(meet_node1)
    ans(meet_node2)

