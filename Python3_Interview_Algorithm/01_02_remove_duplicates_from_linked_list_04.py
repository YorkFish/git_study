#!/usr/bin/env python3
#coding:utf-8

# 01_02 的前三个程序是无序链表，这个针对有序链表
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

def removeDup(head):
    """
    方法功能：对带头结点的有序单链表删除重复的结点
    输入参数：head: 链表头结点
    """
    if head is None or head.next is None:
        return
    
    cur = head.next
    # while cur is not None and cur.next is not None:
    while cur.next is not None:
        if cur.val == cur.next.val :
            cur.next = cur.next.next
        else:
            cur = cur.next
    return None

def constructLinkedList(n):
    """
    方法功能：创建单链表
    说明：上方的 removeDup() 对于升序、降序均有效，不妨建一个升序链表
    """
    head = LNode()
    cur = head
    for i in range(n):
        tmp = LNode()
        if i % 2 == 0:
            tmp.val = i
        else:
            tmp.val = i - 1
        cur.next = tmp
        cur = tmp
    return head

def printLinkedList(head):
    """ 打印单链表 """
    cur = head.next
    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
    print()
    return None

if __name__ == "__main__":
    print("before:")
    head = constructLinkedList(7)
    printLinkedList(head)
    print("\nafter:")
    removeDup(head)
    printLinkedList(head)

