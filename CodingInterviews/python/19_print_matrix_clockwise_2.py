#!/usr/bin/env python3
# coding:utf-8


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        #  -- y
        # |
        # x
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y = 0, 0
        d = 0  # direction
        row = len(matrix)
        col = len(matrix[0])
        times = row * col
        res = [[0] * col for _ in range(row)]
        ans = [0] * times
        for i in range(times):
            res[x][y] = matrix[x][y]
            ans[i] = res[x][y]
            temp_x = x + dx[d]
            temp_y = y + dy[d]
            if (temp_x < 0 or temp_x == row or temp_y < 0 or temp_y == col
                    or res[temp_x][temp_y]):
                d = (d + 1) % 4
                temp_x = x + dx[d]
                temp_y = y + dy[d]
            x, y = temp_x, temp_y
        return ans


if __name__ == "__main__":
    array = [[1, 2], [3, 4]]

    s = Solution()
    ans = s.printMatrix(array)
    print(ans)
