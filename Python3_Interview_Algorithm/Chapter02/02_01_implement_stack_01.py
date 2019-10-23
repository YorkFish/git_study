#!/usr/bin/env python3
#coding:utf-8
class MyStack(object):
    """
    模拟栈
    具体功能：圧栈、弹栈、取栈顶元素、判断栈是否为空、获取栈中元素
    """
    def __init__(self):
        self.items = []

    # 判断栈是否为空
    def isEmpty(self):
        return len(self.items) == 0

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 返回栈顶元素
    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]
        else:
            return None

    # 弹栈
    def pop(self):
        if self.size() > 0:
            print("Out of the stack succeed!")
            return self.items.pop()
        else:
            print("The stack is empty!")
            return None

    # 圧栈
    def push(self, item):
        self.items.append(item)

if __name__ == "__main__":
    s = MyStack()
    s.push(4)
    print("The top element of the stack is:", s.top())
    s.pop()
    s.pop()

