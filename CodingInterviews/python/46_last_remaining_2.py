#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def LastRemaining_Solution(self, n, m):
        """
        f(n) = (f(n-1) + m) % (n-1 peoples)  # n 个人的情况，获胜者的索引
        
        n:   0,   1, ..., m-2, [m-1], m, m+1, ..., (winner), ..., n-1
        n-1: m, m+1, ..., (winner), ...,     n-1, 0, 1, ..., m-2
        ...
        1:   0 <- winner
        根据 (winner) 在 x-1 人的索引，计算其在 x 人的索引，直到 n 人的索引
        """
        if n < 1:
            return -1

        res = 0
        for size in range(2, n + 1):
            res = (res + m) % size
        return res


if __name__ == "__main__":
    n = 10
    m = 6

    s = Solution()
    ans = s.LastRemaining_Solution(n, m)
    print(ans)
