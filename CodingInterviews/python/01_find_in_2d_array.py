#!/usr/bin/env python3
# coding:utf-8


class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = len(array)
        i = 0
        j = len(array[0]) - 1
        while i < row and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


if __name__ == "__main__":
    array = [[1, 3, 4, 5],
             [2, 3, 5, 7],
             [4, 5, 7, 9],
             [6, 7, 9, 10]]
    target1 = 7
    target2 = 8

    s = Solution()
    print(s.Find(target1, array))
    print(s.Find(target2, array))
