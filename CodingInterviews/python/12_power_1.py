#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def Power(self, base, exponent):
        """
        @param: base: double
        @param: exponent: int
        """
        if exponent == 0:
            return 1
        if base == 0:
            return 0

        res = 1
        for _ in range(abs(exponent)):
            res *= base
        return 1 / res if exponent < 0 else res


if __name__ == "__main__":
    s = Solution()
    print(s.Power(2, 0))
    print(s.Power(0, 2))
    print(s.Power(3.5, 2))
    print(s.Power(3.5, -2))
