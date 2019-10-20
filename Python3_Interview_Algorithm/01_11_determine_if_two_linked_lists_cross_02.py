#!/usr/bin/env python3
#coding:utf-8
# import 01_06_check_if_linked_list_has_ring_03 as ring # 模块名带了下划线，不好使
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

# 将 head1 的尾部链到 head2 的头部，形成一个有环单链表，然后可套用 01_06 的解法
def concatenate(head1, head2):
    cur = head1.next
    while cur.next:
        cur = cur.next
    cur.next = head2.next
    return None

def isLoop(head):
    """
    方法功能：判断单链表是否有环
    输入参数：head: 链表头结点
    返回值：无环：None；有环：slow 与 fast 相遇的结点
    """
    if head is None or head.next is None:
        return None

    slow = fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return slow
    return None

def findLoopNode(head, meet_node):
    """
    方法功能：找出环的入口点
    输入参数：head: 链表头结点；meet_node: fast 与 slow 相遇的结点
    返回值：fast 与 slow 相遇的结点
    """
    first = head.next
    second = meet_node
    while first is not second:
        first = first.next
        second = second.next
    return first

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
    head1->1->2->3->4                     head1->1->2->3->4
                     \                                     \
                      ->8->9->10->None =>                   ->8->9->10
                    /                                      /         |
    head2->5->6->7-                                5->6->7-          |
                                                   |                 |
                                                    --------<--------
    """

    concatenate(head1, head2)
    meet_node = isLoop(head1)
    if meet_node:
        # 若只要判断是否交叉，这里就够了；不过 meet_node 不是交点，而是快慢指针在环内的相遇点
        print(f"\nTwo linked lists cross. The intersection value is {meet_node.val}.")

        # 若要找到交叉点，再加上这句
        print(f"The intersection node's value is {findLoopNode(head1, meet_node).val}.")
    else:
        print("\nnon-intersect!")

