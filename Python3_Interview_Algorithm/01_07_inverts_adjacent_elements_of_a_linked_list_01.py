#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

def reverse(head):
    """ 把链表相邻元素翻转 """
    if head is None or head.next is None:
        return None
    odd = head.next
    even = odd.next
    while even:
        odd.val, even.val = even.val, odd.val
        odd = even.next
        if odd is None:
            return None
        even = odd.next
    return None

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
    head1 = constructLinkedList(7)
    printLinkedList(head1)
    reverse(head1)
    printLinkedList(head1)
    print()
 
    head2 = constructLinkedList(8)
    printLinkedList(head2)
    reverse(head2)
    printLinkedList(head2)

