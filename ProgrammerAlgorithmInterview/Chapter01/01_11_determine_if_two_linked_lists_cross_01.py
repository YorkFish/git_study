#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

def intersect(head1, head2):
    """
    方法功能：判断两个无环链表是否相交，若相交，则找出该结点
    输入参数：head1 与 head2 分别为两个链表的头结点
    返回值：若相交，返回该结点；若不相交，则返回 None
    """
    if head1 is None or head1.next is None or head2 is None or head2.next is None:
        return None

    set_hash = set()
    cur = head1.next
    while cur:
        set_hash.add(cur)
        cur = cur.next
    cur = head2.next
    while cur:
        if cur in set_hash:
            return cur
        cur = cur.next
    return None

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

    ans = intersect(head1, head2)
    if ans:
        print(f"Two linked lists cross. The intersection value is {ans.val}.")
    else:
        print("non-intersect!")

