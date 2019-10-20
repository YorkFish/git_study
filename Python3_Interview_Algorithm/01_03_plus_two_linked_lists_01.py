#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

def plusTwoLinkedLists(h1, h2):
    """
    方法功能：对两个带头结点的单链表所代表的的数相加
    输入参数：h1: 第一个链表的头结点；h2: 第二个链表的头结点
    返回值：两个链表所对应的数字相加后的数值
    """
    def linkedListToNum(head):
        """ 将单链表转换成对应的数字 """
        if head is None or head.next is None:
            return 0

        cur = head.next
        num = 0
        magnitude = 1
        while cur is not None:
            num += cur.val * magnitude
            magnitude *= 10
            cur = cur.next
        return num
    
    return linkedListToNum(h1) + linkedListToNum(h2)

def constructLinkedList(nums):
    """
    方法功能：创建单链表
    输入参数：nums: list[int], 按索引顺序，依次为“个位”、“十位”、“百位”……
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
    print("linked list 1:", end=' ')
    head1 = constructLinkedList([3, 1, 5])
    printLinkedList(head1)
    print("linked list 2:", end=' ')
    head2 = constructLinkedList([5, 9, 3])
    printLinkedList(head2)

    print("\nafter plus:", end=' ')
    print(plusTwoLinkedLists(head1, head2))

