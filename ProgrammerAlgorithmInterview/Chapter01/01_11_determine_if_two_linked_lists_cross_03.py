#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

# 其实题目没有要求找出交点，不过练练手也是好的
def isIntersect(head1, head2):
    """
    方法功能：判断两个链表是否相交；若相交，找出交点
    输入参数：head1 与 head2 分别表示两个链表的头结点
    返回值：若相交，返回相交结点；若不相交，返回 None
    """
    if head1 is None or head1.next is None or head2 is None or head2 is None:
        return None

    len_head1, tail1 = lenOfLinkedList(head1)
    len_head2, tail2 = lenOfLinkedList(head2)
    cur1 = head1
    cur2 = head2
    if tail1 is tail2:
        # print("相交") # 若只判断相交，到这儿就可以 return 了

        if len_head1 < len_head2:
            for i in range(len_head2 - len_head1):
                cur2 = cur2.next
        elif len_head2 < len_head1:
            for i in range(len_head1 - len_head2):
                cur1 = cur1.next
        while cur1 is not cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1 # cur1, cur2 都行
    else:
        return None

def lenOfLinkedList(head):
    """
    方法功能：计算非空链表的长度并返回 None 前面一个结点
    输入参数：链表头结点
    返回值：cnt: 链表中带数据的结点的长度；cur: None 前面一个结点
    """
    cur = head
    cnt = 0
    while cur.next:
        cur = cur.next
        cnt += 1
    return cnt, cur

def constructLinkedList(nums):
    """
    方法功能：创建单链表
    输入参数：nums: 作为链表结点的数据
    返回值：head: 链表头结点；tail: 链表尾结点
    """
    head = LNode()
    cur = head
    for num in nums:
        tmp = LNode()
        tmp.val = num
        cur.next = tmp
        cur = tmp
    tail = cur
    return head, tail # 直接返回 (head, cur) 也行，不过这样直观一点

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
    head1, tail1 = constructLinkedList([1, 2, 3, 4])
    head2, tail2 = constructLinkedList([5, 6, 7])
    head3, tail3 = constructLinkedList([8, 9, 10]) # tail3 没有用
    tail1.next = head3.next
    tail2.next = head3.next

    print("head1:", end=' ')
    printLinkedList(head1)
    print("\nhead2:", end=' ')
    printLinkedList(head2)
    """
    head1->1->2->3->4
                     \
                      ->8->9->10->None
                    /
    head2->5->6->7-
    """

    meet_node = isIntersect(head1, head2)
    if meet_node:
        print(f"\nTwo linked lists cross. The intersection value is {meet_node.val}.")
    else:
        print("\nnon-intersect!")

