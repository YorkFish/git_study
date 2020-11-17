#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0

        res = [1] * index
        idx2 = idx3 = idx5 = 0
        cnt = 1
        while cnt < index:
            minVal = min(2 * res[idx2], 3 * res[idx3], 5 * res[idx5])
            res[cnt] = minVal
            cnt += 1
            if minVal == 2 * res[idx2]:
                idx2 += 1
            if minVal == 3 * res[idx3]:
                idx3 += 1
            if minVal == 5 * res[idx5]:
                idx5 += 1
        return res[-1]


if __name__ == "__main__":
    index = 7

    s = Solution()
    ans = s.GetUglyNumber_Solution(index)
    print(ans)
