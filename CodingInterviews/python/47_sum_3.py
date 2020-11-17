#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def Sum_Solution(self, n):
        return n and (n + self.Sum_Solution(n - 1))


if __name__ == "__main__":
    n = 10

    s = Solution()
    ans = s.Sum_Solution(n)
    print(ans)
