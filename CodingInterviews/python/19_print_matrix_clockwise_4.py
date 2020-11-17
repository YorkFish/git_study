#!/usr/bin/env python3
# coding:utf-8


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix:
                matrix = list(zip(*matrix))[::-1]  # 逆时针旋转 90 度；Python2 的 zip 返回 list
        return res


if __name__ == "__main__":
    array = [[1, 2], [3, 4]]

    s = Solution()
    ans = s.printMatrix(array)
    print(ans)
