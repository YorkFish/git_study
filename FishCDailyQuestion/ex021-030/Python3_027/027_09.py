#!/usr/bin/env python3
# coding:utf-8

"""
  1 2 3
  \ | /
4'- + -4
  / | \
3' 2' 1'

由题意得 1, 2, 3, 4 四条路和相等
=> 1 + 1' = 2 + 2' = 3 + 3' = 4 + 4'
  从 1 ~ 9 中取四对数，使其和相等，只能首尾配对
  (1, 9), (2, 8), (3, 7), (4, 6)
=> 中间为 5
=> 每条路的和为 15
=> 九宫图“四条边”每边和也为 15

从上述四对数中在配对前提下取 3 个数作边，仅能凑 4 组
  (1, 6, 8)
  (2, 4, 9), (2, 6, 7)
  (3, 4, 8)
=> 2, 4, 6, 8 均出现两次，故为四角
  2 与 4, 6 搭配，故 2 与 4, 6 相邻，8 为 2 的对角
  剩下的数按上述新的四对补齐即可

严格来说，九宫图只有一种解，其他解均由此解或旋转，或镜像得到
题目给出 1 解，旋转可再得 3 解，镜像后又有 4 解 => 共 8 解
"""


def printGridView(nums):
    global cnt
    cnt += 1
    print(f"No.{cnt}:")
    for i in range(3):
        for j in range(2):
            print(nums[i][j], end=" | ")
        print(nums[i][2], "\n-   -   -")
    print('=' * 10)


def mirror(nums):
    for i in range(3):
        nums[i][0], nums[i][2] = nums[i][2], nums[i][0]


def clockWise(nums):
    res = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            res[j][2-i] = nums[i][j]
    return res


def solve(nums):
    for i in range(2):
        for j in range(4):
            nums = clockWise(nums)
            printGridView(nums)
        mirror(nums)


if __name__ == "__main__":
    nums = [[8, 1, 6], 
            [3, 5, 7],
            [4, 9, 2]]
    cnt = 0
    solve(nums)
