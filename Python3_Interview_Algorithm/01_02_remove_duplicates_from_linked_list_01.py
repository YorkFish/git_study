#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeDup(head):
    """
    方法功能：对带头结点的无序单链表删除重复的结点
    输入参数：head: 链表头结点
    """
    if head is None or head.next is None:
        return

    outer_cur = head.next # 用于外层循环，指向链表第一个结点
    inner_cur = None # 用于内层循环，用来遍历 outerCur 后面的结点
    inner_pre = None # innerCur 的前驱结点
    while outer_cur is not None:
        inner_cur = outer_cur.next
        inner_pre = outer_cur
        while inner_cur is not None:
            if outer_cur.val == inner_cur.val: # 若找到重复结点，则删除
                inner_pre.next = inner_cur.next
                inner_cur = inner_cur.next
            else:
                inner_pre = inner_cur
                inner_cur = inner_cur.next
        outer_cur = outer_cur.next
    return None

def constructLinkedList(n):
    """ 创建单链表 """
    head = LNode(None)
    # head.next = None
    tmp = None
    cur = head
    for i in range(1, n):
        tmp = LNode(None)
        if i % 2 == 0:
            tmp.val = i + 1
        elif i % 3 == 0:
            tmp.val = i - 2
        else:
            tmp.val = i
        # tmp.next = None
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
    print("after:")
    removeDup(head)
    printLinkedList(head)

