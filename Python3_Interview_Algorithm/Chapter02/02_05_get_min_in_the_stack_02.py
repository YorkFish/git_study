#!/usr/bin/env python3
#coding:utf-8
# 其实这个程序只是对 02_05 的第一个程序做了一丁点小改动
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
        if self.getSize():
            return self.items.pop()
        print("The stack is empty.")
        return None

    def push(self, item):
        """ 圧栈 """
        self.items.append(item)
        return None

class MyStack(object):
    """ 存储“历代”最小值 """
    def __init__(self):
        self.elemStack = Stack() # 用来存储栈中元素
        self.minStack = Stack() # 栈顶永远存储当前 elemStack 中最小的值

    def push(self, data):
        """ 圧栈 """
        self.elemStack.push(data)
        if self.minStack.isEmpty():
            self.minStack.push(data)
        elif data <= self.minStack.peek(): # 我觉得需要加上等于号，防止数据有重复
            self.minStack.push(data)
        return None

    def pop(self):
        """ 弹栈 """
        top_data = self.elemStack.pop()
        if top_data == self.mins():
            self.minStack.pop()
        return top_data

    def mins(self):
        """ 返回“最小值栈”的栈顶（若有） """
        if self.minStack.isEmpty():
            return None # 题目中有提 int，但 2**32 在这里并不溢出，不如写 None 或 float("-inf")
        return self.minStack.peek()

if __name__ == "__main__":
    stack = MyStack()
    #stack.push(5)
    #print("The min value of stack is:", stack.mins())
    #stack.push(6)
    #print("The min value of stack is:", stack.mins())
    #stack.push(2)
    #print("The min value of stack is:", stack.mins())
    #stack.pop()
    #print("The min value of stack is:", stack.mins())
    stack.push(5)
    stack.push(4)
    stack.push(2)
    stack.push(2)
    stack.push(1)
    print("The min value of stack is:", stack.mins())
    stack.pop()
    stack.pop()
    print("The min value of stack is:", stack.mins())

