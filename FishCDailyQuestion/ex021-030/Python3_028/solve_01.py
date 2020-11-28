#!/usr/bin/env python3
# coding:utf-8

"""
个人拙见：
1. 数字可重复使用，如 (5, 5, 5)
2. (4, 5, 6) 与 (6, 5, 4) 为一种解

令左、中、右（单调不减）三个数字为 l, m, r
 / l + m >= 15 - 9 => m >= 3
|                             => 3 <= m <= 7  => m = 5 时，l 取得最大值 5
 \ m + r <= 15 - 1 => m <= 7
r 可由 15 - l - m 得到
"""


def solve():
    cnt = 0
    for m in range(3, 8):
        for l in range(1, 6):
            r = 15 - l - m
            if r > 9:
                continue
            elif r < m or m < l:
                break
            else:
                cnt += 1
                print(f"No.{cnt:0>2}: {l} {m} {r}")


if __name__ == "__main__":
    solve()
