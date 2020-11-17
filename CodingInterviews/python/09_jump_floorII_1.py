#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def jumpFloorII(self, number):
        return pow(2, number - 1)  # 若 number 可能为 0，则需要特判


if __name__ == "__main__":
    n = 0

    s = Solution()
    ans = s.jumpFloorII(n)
    print(ans)
