#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def getSingleSum(self, num):
        res = 0
        while num:
            res += num % 10
            num //= 10
        return res

    def getSum(self, x, y):
        return self.getSingleSum(x) + self.getSingleSum(y)

    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows < 0 or cols < 0:
            return 0

        used = [[False] * cols for _ in range(rows)]
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        q = [(0, 0)]
        res = 0
        while q:
            x, y = q.pop(0)
            if (used[x][y] or threshold < self.getSum(x, y)):
                continue
            res += 1
            used[x][y] = True

            for i in range(4):
                tmpX = x + dx[i]
                tmpY = y + dy[i]
                if 0 <= tmpX < rows and 0 <= tmpY < cols:
                    q.append((tmpX, tmpY))
        return res


if __name__ == "__main__":
    threshold = 18
    rows = 50
    cols = 50

    s = Solution()
    ans = s.movingCount(threshold, rows, cols)
    print(ans)
