#!/usr/bin/env python3
#coding:utf-8
from random import randint

class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

def merge(head1, head2):
    """
    方法功能：合并两个升序排列的单链表
    输入参数：head1 与 head2 代表两个单链表
    返回值：合并后链表的头结点
    """
    if head1 is None or head1.next is None:
        return head2
    elif head2 is None or head2.next is None:
        return head1

    cur1 = head1.next # 用来遍历 head1
    cur2 = head2.next # 用来遍历 head2
    
    # head: 用作合并后的链表的头结点，直接用原链表的，省得自己新建
    # cur: 用作合并时链表的实时的尾结点
    if cur1.val < cur2.val:
        head = head1
        cur = cur1
        cur1 = cur1.next
    else:
        head = head2
        cur = cur2
        cur2 = cur2.next

    # 若两个链表的“指针”均未指向各自尾部，就继续“归并”
    while cur1 and cur2:
        if cur1.val < cur2.val:
            cur.next = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur = cur2
            cur2 = cur2.next

    # 若遍历完链表 a，而链表 b 有多，就将 b 剩余的结点一并链到合并链表的后面
    if cur1:
        cur.next = cur1
    elif cur2:
        cur.next = cur2
    return head

def constructLinkedList(nums):
    """
    方法功能：创建单链表
    输入参数：nums: list[int] 列表中的数据已按照升序排列，作为链表中的结点数据
    """
    head = LNode()
    cur = head
    for num in nums:
        tmp = LNode()
        tmp.val = num
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
    print("linked list 1:", end=' ')
    lst1 = [randint(1, 50) for i in range(5)]
    lst1.sort()
    head1 = constructLinkedList(lst1)
    printLinkedList(head1)

    print("\nlinked list 2:", end=' ')
    lst2 = [randint(1, 50) for i in range(5)]
    lst2.sort()
    head2 = constructLinkedList(lst2)
    printLinkedList(head2)

    print("\nafter merge:", end=' ')
    head = merge(head1, head2)
    printLinkedList(head)

