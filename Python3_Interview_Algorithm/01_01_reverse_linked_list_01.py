#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head):
    """
    方法功能：对单链表进行逆序
    输入参数：head: 链表头结点
    """
    if head == None or head.next == None: # 链表为空或只有头结点
        return

    # 初始化
    pre = None # 前驱结点
    cur = None # 当前结点
    nxt = None # 后继结点

    # 把链表首结点变为尾结点
    cur = head.next
    nxt = cur.next
    cur.next = None
    pre = cur
    cur = nxt

    # 使当前遍历到的结点 cur 指向其前驱结点
    while cur.next != None:
        nxt = cur.next
        cur.next = pre
        pre = cur
        # cur = cur.next
        cur = nxt

    cur.next = pre # 链表最后一个结点指向倒数第二个结点
    head.next = cur # 链表的头结点指向原来链表的尾结点

def printLinkedList(head):
    cur = head.next
    while cur != None:
        print(cur.data, end=' ')
        cur = cur.next
    print()

if __name__ == "__main__":
    head = LNode(None)
    head.next = None

    # 构造单链表
    cur = head
    tmp = None
    for i in range(8):
        tmp = LNode(None)
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
    
    print("before:")
    printLinkedList(head)

    reverse(head)
    print("\nafter:")
    printLinkedList(head)
    
