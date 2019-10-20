#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

def removeDup(head):
    """
    方法功能：对带头结点的无序单链表删除重复的结点
    输入参数：head: 链表头结点
    """
    if head is None or head.next is None:
        return
    
    hash_set = set()
    pre = head
    cur = head.next
    while cur is not None:
        if cur.val in hash_set:
            pre.next = cur.next
        else:
            hash_set.add(cur.val)
            pre = pre.next
        cur = cur.next
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

