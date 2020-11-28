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
    返回值：相加后链表的头结点
    """
    def extraNodes(cur, p, carry):
        """ 将多余的结点按规则加入相加链表 """
        while cur is not None:
            tmp = LNode()
            sums = cur.val + carry
            tmp.val = sums % 10
            carry = sums // 10
            p.next = tmp
            p = tmp
            cur = cur.next
        if carry == 1:
            tmp = LNode()
            tmp.val = 1
            p.next = tmp
        return None

    if h1 is None or h1.next is None:
        return h2
    elif h2 is None or h2.next is None:
        return h1

    carry = 0 # 记录进位
    sums = 0 # 记录两个结点相加的值
    p1 = h1.next # 用来遍历 h1
    p2 = h2.next # 用来遍历 h2
    tmp = None # 用来指向新创建的存储相加和的结点
    result_head = LNode() # 相加链表的头结点
    p = result_head # 用来指向链表 result_head 最后一个非空结点
    while p1 is not None and p2 is not None:
        tmp = LNode()
        sums = p1.val + p2.val + carry
        tmp.val = sums % 10 # 两结点相加和
        carry = sums // 10 # 进位
        p.next = tmp
        p = tmp
        p1 = p1.next
        p2 = p2.next
    
    if p1 is None and p2 is None:
        return result_head
    elif p1 is None: # 链表 h1 比 h2 短，接下来只需要考虑 h2 剩余结点的值
        extraNodes(p2, p, carry)
    else: # 链表 h2 比 h1 短，接下来只需要考虑 h1 剩余结点的值
        extraNodes(p1, p, carry)
    return result_head

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
    head1 = constructLinkedList([3, 4, 5, 6, 7, 8])
    printLinkedList(head1)
    print("linked list 2:", end=' ')
    head2 = constructLinkedList([9, 8, 7, 6, 5])
    printLinkedList(head2)

    print("\nafter plus:", end=' ')
    printLinkedList(plusTwoLinkedLists(head1, head2))

