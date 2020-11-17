#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def NumOf1(self, n):
        cnt = 0
        mask = 1
        for _ in range(32):
            if n & mask != 0:
                cnt += 1
            mask <<= 1
        return cnt


if __name__ == "__main__":
    s = Solution()
    print(s.NumOf1(100))
    print(s.NumOf1(-100))
