#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k or k <= 0:
            return []

        def createMaxHeap(num):
            """create or add"""
            maxHeap.append(num)
            curIdx = len(maxHeap) - 1
            while curIdx > 0:
                parentIdx = curIdx - 1 >> 1
                if maxHeap[parentIdx] < maxHeap[curIdx]:
                    maxHeap[parentIdx], maxHeap[curIdx] =\
                        maxHeap[curIdx], maxHeap[parentIdx]
                    curIdx = parentIdx
                else:
                    break

        def adjustMaxHeap(num):
            if num < maxHeap[0]:
                maxHeap[0] = num
            idx = 0
            largerIdx = 0
            while idx < k:
                leftIdx = idx * 2 + 1
                rightIdx = idx * 2 + 2
                if rightIdx < k:
                    if maxHeap[rightIdx] < maxHeap[leftIdx]:
                        largerIdx = leftIdx
                    else:
                        largerIdx = rightIdx
                elif leftIdx < k:
                    largerIdx = leftIdx
                else:
                    break
                if maxHeap[idx] < maxHeap[largerIdx]:
                    maxHeap[idx], maxHeap[largerIdx] =\
                        maxHeap[largerIdx], maxHeap[idx]
                idx = largerIdx

        maxHeap = []
        for i in range(k):
            createMaxHeap(tinput[i])
        for i in range(k, len(tinput)):
            adjustMaxHeap(tinput[i])
        return sorted(maxHeap)


if __name__ == "__main__":
    nums = [4, 5, 1, 6, 2, 7, 3, 8]
    k = 4

    s = Solution()
    ans = s.GetLeastNumbers_Solution(nums, k)
    print(ans)
