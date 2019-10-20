#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

def remove(r_node):
    """
    方法功能：给定单链表中某个结点，删除该节点
    输入参数：链表中某结点
    返回值：true: 删除该结点；false: 删除失败
    """
    # 若输入结点为空或该结点无后继结点，则无法删除；因为实际上是删除后继结点
    if r_node is None or r_node.next is None:
        return False

    r_node.val = r_node.next.val
    r_node.next = r_node.next.next
    return True

def constructLinkedList(n, random_num):
    """
    方法功能：创建单链表
    输入参数：n: 不算头结点 head 与尾部的 None，结点的长度；random_num: 用来指向某个结点
    返回值：head：建成的链表的头结点；random_node: 某个结点
    """
    head = LNode()
    cur = head
    for i in range(1, n+1):
        tmp = LNode()
        tmp.val = i
        cur.next = tmp
        cur = tmp
        if i == random_num:
            random_node = cur
    return head, random_node

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
    head, r_node = constructLinkedList(7, 5)
    print("before:", end=' ')
    printLinkedList(head)

    print("\nafter:", end=' ')
    remove(r_node)
    printLinkedList(head)

