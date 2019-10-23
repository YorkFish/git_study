#!/usr/bin/env python3
#coding:utf-8
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
        else:
            return self.items.pop()

    def push(self, item):
        """ 圧栈 """
        self.items.append(item)
        return None

def isPopSerial(push, pop):
    """ 判断出栈顺序是否合法 """
    if push is None or pop is None:
        return False

    push_len = len(push)
    pop_len = len(pop)
    if push_len != pop_len:
        return False

    push_index = 0
    pop_index = 0
    stack = Stack()
    while push_index < push_len:
        stack.push(push[push_index]) # 把 push 序列依次入栈，直到栈顶元素等于 pop 序列的第一个元素
        push_index += 1 # 栈顶元素出栈，pop 序列移动到下一个元素
        while not stack.isEmpty() and stack.peek() == pop[pop_index]:
            stack.pop()
            pop_index += 1
    # 栈为空，且 pop 序列中元素都被遍历过
    return stack.isEmpty() #and pop_index == pop_len

def ans(push, pop):
    if isPopSerial(push, pop):
        print(f"{pop} is one of the {push} sequences.")
    else:
        print(f"{pop} is not one of the {push} sequences.")
    return None

if __name__ == "__main__":
    push = "12345"
    pop1 = "32541"
    pop2 = "53412"
    ans(push, pop1)
    ans(push, pop2)

