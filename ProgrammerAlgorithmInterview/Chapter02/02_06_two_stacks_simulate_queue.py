#!/usr/bin/env python3
#coding:utf-8
class Stack(object):
    """ 模拟栈 """
    def __init__(self):
        self.items = []

    def getSize(self):
        """ 返回栈的大小 """
        return len(self.items)

    def isEmpty(self):
        """ 判断栈是否为空 """
        return self.getSize() == 0

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

class MyQueue(object):
    """ 模拟队列 """
    def __init__(self):
        self.A = Stack() # 用来存储栈中元素
        self.B = Stack() # 用来存储当前栈中最小元素

    def push(self, data):
        """ 入队 """
        self.A.push(data)
        return None

    def pop(self):
        """ 出队 """
        if self.A.isEmpty() and self.B.isEmpty(): # 以防万一，加一句
            return None
        elif self.B.isEmpty():
            while not self.A.isEmpty():
                self.B.push(self.A.pop())
        return self.B.pop()

if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print("The beginning data of the queue is", queue.pop())
    print("The beginning data of the queue is", queue.pop())

