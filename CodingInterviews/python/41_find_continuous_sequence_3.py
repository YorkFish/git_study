#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def FindContinuousSequence(self, tsum):
        l, r = 1, 2
        tmpSum = 3
        res = []
        while l < r:
            if tmpSum > tsum:
                tmpSum -= l
                l += 1
            else:
                if tmpSum == tsum:
                    res.append([i for i in range(l, r + 1)])
                r += 1
                tmpSum += r
        return res


if __name__ == "__main__":
    tsum = 3

    s = Solution()
    ans = s.FindContinuousSequence(tsum)
    print(ans)
