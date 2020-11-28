#!/usr/bin/env python3
#coding:utf-8

# 01_05 前两个程序是找倒数第 k 个元素；这个程序是将单链表向右旋转 k 个位置
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

def rotateK(head, k):
    """
    方法功能：把链表右旋 k 个位置
    输入参数：head: 链表头结点；k: 需要旋转的次数
    """
    if k < 1 or head is None or head.next is None:
        return None

    # fast 先走 k 步，然后与 slow 一起向后走
    slow = fast = head.next
    i = 0
    while i < k and fast is not None: # 前移 k 步
        fast = fast.next
        i += 1
    if i < k: # 判断 k 是否已经超出链表长度
        return # 我觉得这里可以改进，右旋没有超不超出，多余的长度可以继续旋嘛

    # 下方循环结束后，slow 指向链表倒数第 k+1 个元素，fast 指向链表最后一个非空元素
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    
    tmp = slow
    slow = slow.next
    tmp.next = None
    fast.next = head.next
    head.next = slow
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
    head = constructLinkedList([i for i in range(1, 8)])
    printLinkedList(head)
    
    print("\nafter:", end=' ')
    rotateK(head, 3)
    printLinkedList(head)

