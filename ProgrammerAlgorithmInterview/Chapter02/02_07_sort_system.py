#!/usr/bin/env python3
#coding:utf-8
from collections import deque

class User(object):
    def __init__(self, id_num, name):
        self.id_num = id_num # 唯一标识一个用户
        self.name = name
        self.seq = 0

    def getName(self):
        """ 获取姓名 """
        return self.name

    def setName(self):
        """ 设置姓名 """
        self.name = name

    def getSeq(self):
        """ 获取排名 """
        return self.seq

    def setSeq(self, seq):
        """ 设置排名 """
        self.seq = seq

    def getId(self):
        """ 获取 id number """
        return self.id_num

    def equals(self, arg0):
        """ 判断 id number 是否相等 """
        return self.id_num == arg0.getId()

    def toString(self):
        """ 输出结果字符串 """
        return f"id: {self.id_num}; name: {self.name}; seq: {self.seq}"

class MyQueue(object):
    def __init__(self):
        self.q = deque()

    def enQueue(self, u):
        """ 正常入队 """
        self.q.append(u)
        u.setSeq(len(self.q))

    def deQueue(self):
        """ 正常出队 """
        self.q.popleft()
        self.updateSeq()

    def deQueueMove(self, u):
        """
        队列中的人随机离开
        开个玩笑：意外发现传说中的“中出数据结构”
        """
        self.q.remove(u)
        self.updateSeq()

    def updateSeq(self):
        """ 有人出队，则更新队列中每人的排名 """
        i = 1
        for u in self.q:
            u.setSeq(i)
            i += 1

    def printQueue(self):
        """ 打印队列的信息 """
        for u in self.q:
            print(u.toString())

if __name__ == "__main__":
    u1 = User(1, "user1")
    u2 = User(2, "user2")
    u3 = User(3, "user3")
    u4 = User(4, "user4")
    queue = MyQueue()
    queue.enQueue(u1)
    queue.enQueue(u2)
    queue.enQueue(u3)
    queue.enQueue(u4)
    queue.printQueue()

    print('-' * 30)
    queue.deQueue() # 队首元素 u1 出列
    queue.printQueue()
    print('-' * 30)
    queue.deQueueMove(u3) # 队中元素 u3 出列
    queue.printQueue()

