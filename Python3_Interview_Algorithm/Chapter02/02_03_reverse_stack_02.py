#!/usr/bin/env python3
#coding:utf-8
from copy import deepcopy

class Stack(object):
    """ 模拟栈 """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """ 判断栈是否为空 """
        return len(self.items) == 0

    def getSize(self):
        """ 返回栈的大小 """
        return len(self.items)

    def peek(self):
        """ 返回栈顶元素 """
        if self.isEmpty():
            return None
        return self.items[-1]

    def pop(self):
        """ 弹栈 """
        if self.isEmpty():
            print("The stack is empty.")
            return None
        return self.items.pop()

    def push(self, item):
        """ 圧栈 """
        self.items.append(item)
        return None

def moveMin2Top(s):
    """
    方法功能：把栈中最小的元素移动到栈顶
    输入参数：s 栈的引用
    """
    if s.isEmpty():
        return

    top1 = s.pop()
    """
    # 方法一
    if s.isEmpty():
        s.push(top1)
    else:
        moveMin2Top(s)
        top2 = s.peek()
        if top2 < top1:
            s.pop()
            s.push(top1)
            s.push(top2)
        else:
            s.push(top1)
    return None
    """
    # 方法二
    if not s.isEmpty():
        moveMin2Top(s) # 将子栈的最小值移到其栈顶
        top2 = s.peek()
        if top2 < top1: # 若子栈的栈顶小于原栈的栈顶，则将其二者换位
            s.pop()
            s.push(top1)
            s.push(top2)
            return
    s.push(top1)
    return

def sortStack(s):
    """ 给栈的元素排序，从栈顶到栈尾，按元素大小的升序排列 """
    if s.isEmpty():
        return

    moveMin2Top(s)
    top = s.pop()
    sortStack(s)
    s.push(top)
    return None

def printStack(s):
    """ 打印栈的元素 """
    print("Top", end="->")
    while not s.isEmpty():
        print(s.pop(), end="->")
    print("Bottom")
    return None

if __name__ == "__main__":
    s = Stack()

    print("before:", end=' ')
    s.push(1)
    s.push(3)
    s.push(5)
    s.push(2)
    s.push(4)
    printStack(deepcopy(s))

    print("\nafter:", end=' ')
    sortStack(s)
    printStack(s)


