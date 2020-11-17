#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if path == '' or rows * cols < len(path):
            return False

        def findPath(matrix, i, j, path):
            if path == '':
                return True
            if (i < 0 or i == rows or j < 0 or j == cols or
                    matrix[i][j] != path[0]):
                return False

            matrix[i][j] = '#'
            isFound = (findPath(matrix, i - 1, j, path[1:]) or
                       findPath(matrix, i + 1, j, path[1:]) or
                       findPath(matrix, i, j - 1, path[1:]) or
                       findPath(matrix, i, j + 1, path[1:]))
            matrix[i][j] = path[0]
            return isFound

        newMatrix = [[0] * cols for _ in range(rows)]
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                newMatrix[i][j] = matrix[cnt]
                cnt += 1
        for i in range(rows):
            for j in range(cols):
                if newMatrix[i][j] == path[0]:
                    if findPath(newMatrix, i, j, path):
                        return True
        return False


if __name__ == "__main__":
    # matrix = [
    #     ['A', 'B', 'C', 'E'],
    #     ['S', 'F', 'C', 'S'],
    #     ['A', 'D', 'E', 'E']
    # ]
    matrix = "ABCESFCSADEE"
    rows = 3
    cols = 4
    path = "ABCCED"

    s = Solution()
    ans = s.hasPath(matrix, rows, cols, path)
    print(ans)
