#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def Fibonacci(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a


if __name__ == "__main__":
    n = 5

    s = Solution()
    ans = s.Fibonacci(n)
    print(ans)
