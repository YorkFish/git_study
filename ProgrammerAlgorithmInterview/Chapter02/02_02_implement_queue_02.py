#!/usr/bin/env python3
#coding:utf-8
class LNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

class MyQueue(object):
    """ 具体功能：入队列、出队列、查看队列首尾元素、查看队列大小 """
    def __init__(self):
        """ 分配头结点 """
        self.pHead = None
        self.pEnd = None

    def isEmpty(self):
        """ 判断队列是否为空 """
        if self.pHead is None:
            return True
        else:
            return False

    def size(self):
        """ 获取队列中元素的个数 """
        size = 0
        p = self.pHead
        while p:
            size += 1
            p = p.next
        return size

    def enQueue(self, e):
        """ 入队列，把元素 e 加到队列尾 """
        p = LNode(e)
        if self.pHead is None:
            self.pHead = self.pEnd = p
        else:
            self.pEnd.next = p
            self.pEnd = p
        return None

    def deQueue(self):
        """ 出队列，删除队列首元素 """
        if self.pHead is None:
            print("Out of queue failure. The queue is empty.")
            return None
        # ?
        self.pHead = self.pHead.next
        if self.pHead is None:
            self.pEnd = None
        return None

    def getFront(self):
        """ 取得队列首元素 """
        if self.pHead is None:
            print("Failed to get the first element of the queue. The queue is empty.")
            return None
        return self.pHead.val

    def getBack(self):
        """ 取得队列尾元素 """
        if self.pEnd is None:
            print("Failed to get the end element of the queue. The queue is empty.")
            return None
        return self.pEnd.val

if __name__ == "__main__":
    queue = MyQueue()
    queue.deQueue()
    #queue.enQueue(1)
    #queue.enQueue(2)
    #print("The first element of the queue is:", queue.getFront())
    #print("The end element of the queue is:", queue.getBack())
    #print("The size of the queue is", queue.size())

