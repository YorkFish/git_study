#!/usr/bin/env python3
#coding:utf-8
from collections import deque

class LRU(object):
    """ LRU for Least Recently Used """
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.queue = deque()
        self.hash_set = set()

    def isQueueFull(self):
        """ 判断缓存队列是否已满 """
        return len(self.queue) == self.cache_size

    def enQueue(self, page_num):
        """ 把页号为 page_num 的页缓存到队列中，同时也添加到 Hash 中 """
        if self.isQueueFull(): # 如果队列满了，需要删除队尾的缓存页
            self.hash_set.remove(self.queue.pop())
        self.queue.appendleft(page_num)
        self.hash_set.add(page_num) # 把新缓存的结点同时添加到 hash 表中

    def accessPage(self, page_num):
        """
        当访问某一个 page 的时候会调用这个函数，对于访问的 page 有两种情况:
        1. 如果 page 在缓存队列中，直接把这个结点移动到队首
        2. 如果 page 不在缓存队列中，把这个 page 缓存到队首
        """
        if page_num not in self.hash_set: # 情况 2
            self.enQueue(page_num)
        elif page_num != self.queue[0]: # 情况 1
            self.queue.remove(page_num)
            self.queue.appendleft(page_num)
        # else: 在队首，就不需要操作了

    def printQueue(self):
        """ 打印队列 """
        while len(self.queue):
            print(self.queue.popleft(), end=' ')
        print()

if __name__ == "__main__":
    lru = LRU(3) # 假设缓存的大小为 3

    # 访问 page
    lru.accessPage(1)
    lru.accessPage(2)
    lru.accessPage(5)
    lru.accessPage(1)
    lru.accessPage(6)
    lru.accessPage(7)

    lru.printQueue() # 通过上面的访问序列后，缓存的信息

