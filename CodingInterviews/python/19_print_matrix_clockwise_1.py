#!/usr/bin/env python3
# coding:utf-8



class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        if row == 0 or col == 0:
            return
        
        times = row * col
        res = [0] * times
        row_start, row_stop = 0, row - 1
        col_start, col_stop = 0, col - 1
        idx = 0
        while idx < times:
            if row_start > row_stop: break
            for j in range(col_start, col_stop+1):
                res[idx] = matrix[row_start][j]
                idx += 1
            row_start += 1

            if col_start > col_stop: break
            for j in range(row_start, row_stop+1):
                res[idx] = matrix[j][col_stop]
                idx += 1
            col_stop -= 1

            if row_start > row_stop: break
            for j in range(col_stop, col_start-1, -1):
                res[idx] = matrix[row_stop][j]
                idx += 1
            row_stop -= 1

            if col_start > col_stop: break
            for j in range(row_stop, row_start-1, -1):
                res[idx] = matrix[j][col_start]
                idx += 1
            col_start += 1
        return res


if __name__ == "__main__":
    array = [[1], [2], [3], [4], [5]]

    s = Solution()
    ans = s.printMatrix(array)
    print(ans)
