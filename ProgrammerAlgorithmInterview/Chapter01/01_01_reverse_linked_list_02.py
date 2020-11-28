#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def recursiveReverse(head):
    """
    方法功能：对不带头结点的单链表进行逆序
    输入参数：firstRef: 链表头结点
    """
    if head == None or head.next == None: # 链表为空或只有一个元素
        return head
    else:
        new_head = recursiveReverse(head.next) # 反转后面的结点
        head.next.next = head # 把当前遍历到的结点加到 new_head 这条逆序后的新链表的尾部
        head.next = None
    return new_head

def reverse(head):
    """
    方法功能：对带头结点的单链表进行逆序
    输入参数：head: 链表头结点
    """
    if head is None:
        return

    first_node = head.next # 获取链表的第一个结点
    new_head = recursiveReverse(first_node) # 对链表进行逆序
    head.next = new_head # 将头结点指向逆序后的第一个结点
    return new_head

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

