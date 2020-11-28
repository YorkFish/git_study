#!/usr/bin/env python3
#coding:utf-8
# Python 中没有栈的模块，所以先新建一个栈类
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
        if len(self.items):
            return self.items.pop()
        print("The stack is empty.")
        return None

    def push(self, item):
        """ 圧栈 """
        self.items.append(item)
        return None

def moveBottom2Top(s):
    """
    方法功能：把栈底元素移动到栈顶
    输入参数：s 栈的引用
    """
    if s.isEmpty():
        return

    top1 = s.pop()
    if s.isEmpty():
        s.push(top1)
    else:
        moveBottom2Top(s) # 递归处理不包含栈顶元素的子栈
        top2 = s.pop()
        s.push(top1) # 交换栈顶元素与子栈栈顶元素
        s.push(top2)
    return None

def reverseStack(s):
    """ 翻转栈的所有元素 """
    if s.isEmpty():
        return

    moveBottom2Top(s) # 把栈底元素移动到栈顶
    top = s.pop()
    reverseStack(s) # 递归处理子栈
    s.push(top)
    return None

def printStack(s):
    """ 打印栈的元素 """
    print("Top", end="->")
    while not s.isEmpty():
        print(s.pop(), end="->")
    print("->Bottom")
    return None

if __name__ == "__main__":
    s = Stack()

    print("before:", end=' ')
    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    printStack(deepcopy(s))

    print("\nafter:", end=' ')
    reverseStack(s)
    printStack(s)

