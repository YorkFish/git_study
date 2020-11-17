#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0

        a, b = 0, 1
        for _ in range(number):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    n = 2

    s = Solution()
    ans = s.rectCover(n)
    print(ans)
