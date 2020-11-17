#!/usr/bin/env python3
# coding:utf-8

from random import randrange


class Solution:
    def __init__(self):
        """
        最小值放大顶堆
        最大值放小顶堆
        """
        self.littleValMaxHeap = []
        self.bigValMinHeap = []
        self.maxHeapCount = 0
        self.minHeapCount = 0

    def Insert(self, num):
        def cmpMinHeap(t, p):
            return t < p

        def cmpMaxHeap(t, p):
            return p < t

        if self.minHeapCount < self.maxHeapCount:
            self.minHeapCount += 1
            if num < self.littleValMaxHeap[0]:
                self.createHeap(self.bigValMinHeap,
                                self.littleValMaxHeap[0],
                                cmpMinHeap)
                self.adjustHeap(self.littleValMaxHeap, num, cmpMaxHeap)
            else:
                self.createHeap(self.bigValMinHeap, num, cmpMinHeap)
        else:
            self.maxHeapCount += 1
            if len(self.littleValMaxHeap) == 0:
                self.createHeap(self.littleValMaxHeap, num, cmpMaxHeap)
            elif self.bigValMinHeap[0] < num:
                self.createHeap(self.littleValMaxHeap,
                                self.bigValMinHeap[0],
                                cmpMaxHeap)
                self.adjustHeap(self.bigValMinHeap, num, cmpMinHeap)
            else:
                self.createHeap(self.littleValMaxHeap, num, cmpMaxHeap)

    def GetMedian(self, n=None):  # add "n=None" because of bad setting
        if self.maxHeapCount == 0:
            return -1
        elif self.minHeapCount < self.maxHeapCount:
            return self.littleValMaxHeap[0]
        else:
            return (self.littleValMaxHeap[0] + self.bigValMinHeap[0]) / 2.0

    def createHeap(self, heap, num, cmpFun):
        heap.append(num)
        tmpIdx = len(heap) - 1
        while tmpIdx > 0:
            parentIdx = (tmpIdx - 1) >> 1
            if cmpFun(heap[tmpIdx], heap[parentIdx]):
                heap[tmpIdx], heap[parentIdx] = heap[parentIdx], heap[tmpIdx]
                tmpIdx = parentIdx
            else:
                break

    def adjustHeap(self, heap, num, cmpFun):
        size = len(heap)
        heap[0] = num
        tmpIdx = 0
        while tmpIdx < size:
            leftIdx = tmpIdx*2 + 1
            rightIdx = tmpIdx*2 + 2
            if rightIdx < size:
                if cmpFun(heap[leftIdx], heap[rightIdx]):
                    target = leftIdx
                else:
                    target = rightIdx
            elif leftIdx < size:
                    target = leftIdx
            else:
                break
            if cmpFun(heap[target], heap[tmpIdx]):
                heap[target], heap[tmpIdx] = heap[tmpIdx], heap[target]
                tmpIdx = target
            else:
                break


if __name__ == "__main__":
    s = Solution()
    # nums = [randrange(10, 100) for num in range(15)]
    nums = [5, 2, 3, 4, 1, 6, 7, 0, 8]
    print(f">>> nums    = {nums}")
    print(f">>> Midian  =  {s.GetMedian()}")
    for num in nums:
        s.Insert(num)
    print(f">>> MinHeap =     {s.bigValMinHeap}")
    print(f">>> MaxHeap = {s.littleValMaxHeap}")
    print(f">>> Midian  =  {s.GetMedian()}")
