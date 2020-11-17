#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def NumOf1(self, n):
        cnt = 0
        while n:
            cnt += 1
            n -= n & -n  # 将最低位的 1 置零
            n &= 0xffffffff
        return cnt


if __name__ == "__main__":
    s = Solution()
    print(s.NumOf1(100))
    print(s.NumOf1(-100))
