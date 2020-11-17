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
        elif base == 0:
            return 0
        
        exp = abs(exponent)
        tmp = base
        res = 1
        while exp:
            if exp & 1 == 1:
                res *= tmp
            exp >>= 1
            tmp *= tmp
        return res if exponent > 0 else 1 / res


if __name__ == "__main__":
    s = Solution()
    print(s.Power(2, 0))
    print(s.Power(0, 2))
    print(s.Power(3.5, 2))
    print(s.Power(3.5, -2))
