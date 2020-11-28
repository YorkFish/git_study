#!/usr/bin/env python3
#coding:utf-8
class MyQueue(object):
    """ 具体功能：入队列、出队列、查看队列首尾元素、查看队列大小 """
    def __init__(self):
        self.arr = []
        self.front = 0 # 队列头
        self.rear = 0 # 队列尾

    def isEmpty(self):
        """ 判断队列是否为空 """
        return self.front == self.rear

    def size(self):
        """ 返回队列的大小 """
        return self.rear - self.front

    def getFront(self):
        """ 返回队列首元素 """
        if self.isEmpty():
            return None
        return self.arr[self.front]

    def getBack(self):
        """ 返回队列尾元素 """
        if self.isEmpty():
            return None
        return self.arr[self.rear - 1]

    def deQueue(self):
        """ 删除队列头元素 """
        if self.front < self.rear:
            self.front += 1
        else:
            print("The queue is empty.")
        return None

    def enQueue(self, item):
        """ 把元素加入队列尾 """
        self.arr.append(item)
        self.rear += 1
        return None

if __name__ == "__main__":
    queue = MyQueue()
    queue.enQueue(1)
    queue.enQueue(2)
    print("The first element of the queue is:", queue.getFront())
    print("The end element of the queue is:", queue.getBack())
    print("The size of the queue is", queue.size())

