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
    返回值：False: 无环；True: 有环；None: 输入有误
    """
    if head is None or head.next is None:
        return None

    slow = fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

def constructLinkedListHasRing(n, r):
    """
    方法功能：r=0: 创建有环单链表；r=1: 创建无环单链表
    输入参数：n: 不算头结点 head 与尾部的 None，结点的长度
    """
    head = LNode()
    cur = head
    for i in range(1, n+1):
        tmp = LNode()
        tmp.val = i
        cur.next = tmp
        cur = tmp
    if r == 0:
        cur.next = head.next.next.next
    return head

if __name__ == "__main__":
    head1 = constructLinkedListHasRing(7, 1)
    head2 = constructLinkedListHasRing(7, 0)
    print(isLoop(head1))
    print(isLoop(head2))

