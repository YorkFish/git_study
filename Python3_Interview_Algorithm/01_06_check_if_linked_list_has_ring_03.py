#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

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

def constructLinkedListHasRing(n, r):
    """
    方法功能：r=0: 创建有环单链表；r=1: 创建无环单链表
    输入参数：n: 不算头结点 head 与尾部的 None，结点的长度
    """
    head = LNode()
    cur = head
    for i in range(1, n+1):
        tmp = LNode()
        tmp.val = i
        cur.next = tmp
        cur = tmp
    if r == 0:
        cur.next = head.next.next.next
    return head

def ans(head, meet_node):
    """
    方法功能：若有环，输出环的入口；若无环，打印文字说明无环
    输入参数：head: 链表头结点；meet_node: 快慢“指针”的相遇点
    """
    if meet_node:
        print("The entry of the ring:", findLoopNode(head, meet_node).val)
    else:
        print("There exist no ring.")
    return None

if __name__ == "__main__":
    head1 = constructLinkedListHasRing(7, 1)
    head2 = constructLinkedListHasRing(7, 0)
    meet_node1 = isLoop(head1)
    meet_node2 = isLoop(head2)
    ans(head1, meet_node1)
    ans(head2, meet_node2)
    
