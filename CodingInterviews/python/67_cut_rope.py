#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def cutRope(self, number):
        if number < 3:
            return 1 * (number - 1)

        res = 1
        if number % 3 == 2:
            number -= 2
            res *= 2
        elif number % 3 == 1:
            number -= 4
            res *= 4
        while number:
            res *= 3
            number -= 3
        return res


if __name__ == "__main__":
    length = 58

    s = Solution()
    ans = s.cutRope(length)
    print(ans)
