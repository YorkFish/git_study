#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

class MyStack(object):
    def __init__(self):
        self.val = None
        self.next = None

    # 判断 stack 是否为空。若为空，返回 True；否则，返回 False
    def isEmpty(self):
        if self.next is None:
            return True
        else:
            return False

    # 获取栈中元素的个数
    def size(self):
        size = 0
        p = self.next
        while p:
            p = p.next
            size += 1
        return size

    # 入栈：把 e 放到栈顶
    def push(self, e):
        p = LNode(e)
        p.next = self.next
        self.next = p

    # 出栈：同时返回栈顶元素
    def pop(self):
        tmp = self.next
        if tmp:
            self.next = tmp.next
            print("Pop successfully!")
            return tmp.val
        print("The stack is empty!")
        return None

    # 取得栈顶元素
    def top(self):
        if self.next:
            return self.next.val
        print("The stack is empty!")
        return None

if __name__ == "__main__":
    stack = MyStack()
    stack.push(10)
    print("The top element of the stack is:", stack.top())
    print("The size of the stack is:", stack.size())
    stack.pop()
    stack.pop()

