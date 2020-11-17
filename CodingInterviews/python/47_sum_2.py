#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def Sum_Solution(self, n):
        return __import__("functools").reduce(lambda x, y: x + y, range(n + 1))


if __name__ == "__main__":
    n = 10

    s = Solution()
    ans = s.Sum_Solution(n)
    print(ans)
