#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head):
    """
    方法功能：对带头结点的单链表进行逆序
    输入参数：head: 链表头结点
    """
    if head is None or head.next is None:
        return None
    
    cur = None # 当前结点
    nxt = None # 后继结点
    cur = head.next.next
    head.next.next = None # 设置链表第一个结点为尾结点
    
    while cur is not None: # 把遍历到的结点插入到头结点的后面
        nxt = cur.next
        cur.next = head.next
        head.next = cur
        cur = nxt
    return None

def printLinkedList(head):
    """
    方法功能：输出单链表
    输入参数：head: 链表头结点
    """
    cur = head.next
    while cur != None:
        print(cur.data, end=' ')
        cur = cur.next
    print()
    return None

def constructLinkedList(n):
    """
    方法功能：构造单链表
    输入参数：n: 设定链表长度（不包括头结点）
    """
    head = LNode(None)
    head.next = None

    cur = head
    tmp = None
    for i in range(n):
        tmp = LNode(None)
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
    return head

if __name__ == "__main__":
    head = constructLinkedList(8)
    print("before:")
    printLinkedList(head)

    reverse(head)
    print("\nafter:")
    printLinkedList(head)

