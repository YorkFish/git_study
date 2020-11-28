#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

def findMiddleNode(head):
    """
    方法功能：找出链表的中间结点；把链表从中间结点断成两个子链表
    输入参数：head: 链表头结点
    返回值：链表中间结点
    """
    if head is None or head.next is None:
        return head

    fast = head # 遍历链表的时候，每次向前走两步
    slow = head # 遍历链表的时候，每次向前走一步
    slow_pre = head

    # 当 fast 到链表尾时，slow 恰好指向链表的中间结点
    while fast is not None and fast.next is not None:
        slow_pre = slow
        slow = slow.next
        fast = fast.next.next
    
    slow_pre.next = None # 把链表断开成两个独立的子链表
    return slow

def reverse(head):
    """
    方法功能：对不带头结点的单链表翻转
    输入参数：head: 链表头结点
    """
    if head is None or head.next is None:
        return head

    pre = head # 前驱结点
    cur = head.next # 当前结点
    # nxt = cur.next # 后继结点
    pre.next = None
    while cur is not None: # 使当前遍历到的结点 cur 指向其前驱结点
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre

def reorder(head):
    """
    方法功能：对链表进行排序
    输入参数：head: 链表头结点
    """
    if head is None or head.next is None:
        return

    cur1 = head.next # 前半部分链表第一个结点
    mid = findMiddleNode(head.next)
    cur2 = reverse(mid) # 后半部分链表逆序后的第一个结点
    # tmp = None
    while cur1.next is not None: # 合并两个链表
        tmp = cur1.next
        cur1.next = cur2
        cur1 = tmp
        tmp = cur2.next
        cur2.next = cur1
        cur2 = tmp
    cur1.next = cur2
    return None

def constructLinkedList(nums):
    """
    方法功能：创建单链表
    输入参数：nums: list[int]
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
    cur = head.next
    print("head->", end='')
    while cur is not None:
        print(cur.val, end="->")
        cur = cur.next
    print("None")
    return None

if __name__ == "__main__":
    print("before:", end=' ')
    head = constructLinkedList([1, 2, 3, 4, 5, 6])
    printLinkedList(head)
    
    print("\nafter:", end=' ')
    reorder(head)
    printLinkedList(head)

