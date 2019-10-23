#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

def removeDupRecursion(head):
    """
    方法功能：对不带头结点的无序单链表删除重复的结点
    输入参数：head: 不带头结点的链表的第一个结点
    """
    if head.next is None:
        return head

    # pointer = None
    cur = head
    pointer = removeDupRecursion(head.next) # 删除以 head.next 为首的子链表的重复结点

    # 找出以 head.next 为首的子链表中与 cur 结点数值相同的结点
    while pointer is not None:
        if head.val == pointer.val:
            cur.next = pointer.next
            pointer = cur.next
        else:
            pointer = pointer.next
            cur = cur.next
    return head

def removeDup(head):
    """
    方法功能：对带头结点的无序单链表删除重复的结点
    输入参数：head: 链表头结点
    """
    if head is None:
        return
    head.next = removeDupRecursion(head.next)
    return None

def constructLinkedList(n):
    """ 创建单链表 """
    head = LNode()
    tmp = None
    cur = head
    for i in range(1, n):
        tmp = LNode()
        if i % 2 == 0:
            tmp.val = i + 1
        elif i % 3 == 0:
            tmp.val = i - 2
        else:
            tmp.val = i
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

