#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

"""
引申：若单链表有环，如何判断两个链表是否相交
1. 若一个有环，另一个没环，肯定不相交
2. 若都有环（忽略环为交点的情况），应是先相交，再有环，如下
head1->1->2->3
              \
               ->4->5->6-7
              /     ^    v
head2->11->12-      --<--
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

def isLoop(head):
    """
    方法功能：判断单链表是否有环
    输入参数：head: 链表头结点
    返回值：无环：None；有环：slow 与 fast 相遇的结点
    """
    if head is None or head.next is None:
        return None

    slow = fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return slow
    return None

def findLoopNode(head, meet_node):
    """
    方法功能：找出环的入口点
    输入参数：head: 链表头结点；meet_node: fast 与 slow 相遇的结点
    返回值：fast 与 slow 相遇的结点
    """
    first = head.next
    second = meet_node
    while first is not second:
        first = first.next
        second = second.next
    return first

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

def constructLinkedList(nums):
    """
    方法功能：创建无环单链表
    输入参数：nums: 作为链表结点的数据
    返回值：head: 链表头结点；cur: None 的前一个结点
    """
    head = LNode()
    cur = head
    for num in nums:
        tmp = LNode()
        tmp.val = num
        cur.next = tmp
        cur = tmp
    return head, cur

def constructLinkedListHasRing(nums):
    """
    方法功能：创建有环单链表
    输入参数：nums: 作为链表结点的数据
    返回值：head: 链表头结点
    """
    head = LNode()
    cur = head
    for num in nums:
        tmp = LNode()
        tmp.val = num
        cur.next = tmp
        cur = tmp
    cur.next = head.next.next
    return head

#def printLinkedList(head):
#    """ 打印单链表 """
#    print("head->", end='')
#    cur = head.next
#    while cur:
#        print(cur.val, end="->")
#        cur = cur.next
#    print("None")
#    return None

if __name__ == "__main__":
    head1, tail1 = constructLinkedList([1, 2, 3])
    head2, tail2 = constructLinkedList([11, 12])
    head3 = constructLinkedListHasRing([4, 5, 6, 7])
    tail1.next = head3.next
    tail2.next = head3.next
    
    meet_node1 = isLoop(head1)
    meet_node2 = isLoop(head2)
    if meet_node1 and meet_node2:
        ring_enter = findLoopNode(head1, meet_node1)
        ring_enter.next = None
        if isLoop(head2) is None: # 若能进入这句 if，说明两个链表共享一个环
            print("Two linked lists cross.")
            print(f"The intersection value is {isIntersect(head1, head2).val}.")
        else:
            print("non-intersect!")
    else:
        print("non-intersect!")

