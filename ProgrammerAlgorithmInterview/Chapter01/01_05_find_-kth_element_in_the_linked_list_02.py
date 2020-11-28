#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

def findLastK(head, k):
    """
    方法功能：找出链表倒数第 k 个结点
    输入参数：head: 链表头结点；k: 需要寻找的位置
    返回值：倒数第 k 个结点
    """
    if k < 1 or head is None or head.next is None:
        return None

    slow = fast = head
    for i in range(k):
        fast = fast.next
        if fast is None:
            return None
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow

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
    print("linked list:", end=' ')
    head = constructLinkedList([1, 2, 3, 4, 5, 6])
    printLinkedList(head)
    
    k = 2
    res = findLastK(head, k)
    if res is None:
        print("\nNot such element! Please enter again!")
    else:
        print(f"The {k}th element from the bottom of linked list is: {res.val}")

