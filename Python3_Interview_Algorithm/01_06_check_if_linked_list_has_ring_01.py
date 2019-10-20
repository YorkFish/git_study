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
    返回值：若无环，返回 None；若有环，返回入环结点
    """
    if head is None or head.next is None:
        return None

    hash_set = set()
    cur = head.next
    while cur:
        if cur in hash_set:
            return (True, cur.val)
        else:
            hash_set.add(cur)
            cur = cur.next
    return (False, cur)

def constructLinkedList(n):
    """
    方法功能：创建单链表
    输入参数：n: 非空结点的长度
    """
    head = LNode()
    cur = head
    for i in range(n):
        tmp = LNode()
        tmp.val = i
        cur.next = tmp
        cur = tmp
    return head

def constructLinkedListHasRing(n):
    """
    方法功能：创建有环单链表
    输入参数：n: 非空结点的长度
    """
    mid = n // 2
    head = LNode()
    cur = head
    for i in range(n):
        tmp = LNode()
        tmp.val = i
        cur.next = tmp
        cur = tmp
        if i == mid:
            m = cur
    cur.next = m
    return head

if __name__ == "__main__":
    head1 = constructLinkedList(8)
    head2 = constructLinkedListHasRing(8)
    print(isLoop(head1))
    print(isLoop(head2))

