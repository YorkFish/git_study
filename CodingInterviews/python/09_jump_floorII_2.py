#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def jumpFloorII(self, number):
        """
        f(n)   = f(n-1) + f(n-2) + ... + f(2) + f(1), n >1
        f(n-1) = f(n-2) + f(n-3) + ... + f(1)
        =>
        f(n) = f(n-1) + [f(n-2) + ... + f(1)]
             = 2f(n-1)
        =>
        f(n) = 2^1     * 2f(n-2)
             = 2^2     * 2f(n-3)
             = 2^(n-2) * 2f(1)
             = 2^(n-1)
        """
        if number < 1:
            return 0
        res = 1
        for _ in range(2, number + 1):
            res *= 2
        return res


if __name__ == "__main__":
    n = 1

    s = Solution()
    ans = s.jumpFloorII(n)
    print(ans)
