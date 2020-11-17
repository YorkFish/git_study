#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0

        bottom_up = [0] * (n + 1)
        bottom_up[1] = 1
        for i in range(2, n + 1):
            bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]

        return bottom_up[n]


if __name__ == "__main__":
    n = 5

    s = Solution()
    ans = s.Fibonacci(n)
    print(ans)
