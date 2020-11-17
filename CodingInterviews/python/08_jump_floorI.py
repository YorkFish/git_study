#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def jumpFloor(self, number):
        if number < 1:
            return 0
        if number == 1 or number == 2:
            return number

        a, b = 1, 2
        for _ in range(3, number + 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    n = 5

    s = Solution()
    ans = s.jumpFloor(n)
    print(ans)
