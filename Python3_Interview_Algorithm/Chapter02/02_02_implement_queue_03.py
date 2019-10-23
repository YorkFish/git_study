#!/usr/bin/env python3
#coding:utf-8
# 方法一的引申，把数组做成循环队列
class MyQueue(object):
    """ 具体功能：入队列、出队列、查看队列首尾元素、查看队列大小 """
    def __init__(self):
        self.MAXSIZE = 6 # 队列容量，不过实际上的容量只有 5 
        self.arr = [None] * self.MAXSIZE
        self.front = 0 # 队列头
        self.rear = 0 # 队列尾

    def isEmpty(self):
        """ 判断队列是否为空 """
        return self.front == self.rear

    def isFull(self):
        """ 判断队列是否已满 """
        return (self.rear + 1) % self.MAXSIZE == self.front

    def getSize(self):
        """ 返回队列的大小 """
        if self.front < self.rear:
            return self.rear - self.front
        elif self.front == self.rear:
            return 0
        else:
            return self.MAXSIZE - (self.front - sefl.rear)

    def getFront(self):
        """ 返回队列首元素 """
        if self.isEmpty():
            return False
        return self.arr[self.front]

    def getBack(self):
        """ 返回队列尾元素 """
        if self.isEmpty():
            return False
        return self.arr[self.rear - 1]

    def deQueue(self):
        """ 删除队列头元素 """
        if self.isEmpty():
            print("The queue is empty.")
            return False
        else:
            print("The first element of the queue is:", self.arr[self.front])
            self.front += 1
            return True

    def enQueue(self, item):
        """ 把元素加入队列尾 """
        if self.isFull():
            print("The queue is full.")
            return False
        else:
            self.arr[self.rear] = item
            self.rear = (self.rear + 1) % self.MAXSIZE
            return True
    
    def traverseQueue(self):
        """ 遍历队列 """
        print("traverse queue:", end=' ')
        t = self.front
        while t != self.rear:
            print(self.arr[t], end=' ')
            t = (t + 1) % self.MAXSIZE
        print()
        return None

if __name__ == "__main__":
    queue = MyQueue()
    print("The queue is empty?", queue.isEmpty())
    
    queue.enQueue(1)
    queue.enQueue(2)
    queue.enQueue(3)
    queue.enQueue(4)
    queue.enQueue(5)
    print("The queue is full?", queue.isFull())
    
    queue.traverseQueue()
    print("The first element of the queue is:", queue.getFront())
    print("The end element of the queue is:", queue.getBack())
    print("The size of the queue is", queue.getSize())

    print("append contiune?", queue.enQueue(6))

    queue.deQueue()
    queue.traverseQueue()
    queue.enQueue(6)
    queue.traverseQueue()

