#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        res = 0
        m = 1
        while m <= n:
            res += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m *= 10
        return res


if __name__ == "__main__":
    n = 13

    s = Solution()
    ans = s.NumberOf1Between1AndN_Solution(n)
    print(ans)
