#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

def reverse(head):
    """ 对不带头结点的单链表进行翻转 """
    if head is None or head.next is None:
        return head

    pre = head # 前驱结点
    cur = pre.next # 当前结点
    pre.next = None
    while cur: # 使当前遍历到的结点 cur 指向其前驱结点
        nxt = cur.next # 后继结点
        cur.next = pre
        pre = cur
        cur = nxt
    return pre

def reverseK(head, k):
    """ 对链表中符合条件的结点，以 k 个为一组，进行翻转 """
    if head is None or head.next is None or k < 2:
        return
    i = 1
    pre = head
    begin = pre.next
    # end = None
    pNext = None
    while begin:
        end = begin
        while i < k:
            if end.next is not None:
                end = end.next
            else:
                return
            i += 1
        pNext = end.next
        end.next = None
        pre.next = reverse(begin)
        begin.next = pNext
        pre = begin
        begin = pNext
        i = 1
    return

def constructLinkedList(n):
    """
    方法功能：创建单链表
    输入参数：n: 不算头结点 head 与尾部的 None，结点的长度
    """
    head = LNode()
    cur = head
    for i in range(1, n+1):
        tmp = LNode()
        tmp.val = i
        cur.next = tmp
        cur = tmp
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

if __name__ == "__main__":
    print("before:")
    head = constructLinkedList(7)
    printLinkedList(head)

    print("\nafter:")
    reverseK(head, 3)
    printLinkedList(head)
