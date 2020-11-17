#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def NumOf1(self, n):
        # 负数 -n 的补码：n 的反码 + 1
        return bin(n & 0xffff_ffff).count('1')  # 去掉高位


if __name__ == "__main__":
    s = Solution()
    print(s.NumOf1(100))
    print(s.NumOf1(-100))
