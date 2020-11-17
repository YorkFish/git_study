#!/usr/bin/env python3
# coding:utf-8


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # f[i][j]: pattern[j:] 是否能匹配 s[i:]
        def dp(x, y, s, p):
            if f[x][y] != -1:
                return f[x][y]
            if y == m:
                f[x][y] = x == n
                return f[x][y]
            firstMatch = x < n and (s[x] == p[y] or p[y] == '.')
            if y + 1 < m and p[y + 1] == '*':
                f[x][y] = (dp(x, y + 2, s, p)  # 不用
                           or firstMatch and dp(x + 1, y, s, p))  # 用 n 次
            else:
                f[x][y] = firstMatch and dp(x + 1, y + 1, s, p)  # 用一次
            return f[x][y]

        n = len(s)
        m = len(pattern)
        f = [[-1] * (m + 1) for _ in range(n + 1)]
        return dp(0, 0, s, pattern)


if __name__ == "__main__":
    string = "aaa"
    p1 = "a.a"
    p2 = "ab*ac*a"
    p3 = "aa.a"
    p4 = "ab*a"

    s = Solution()
    print(s.match(string, p1))
    print(s.match(string, p2))
    print(s.match(string, p3))
    print(s.match(string, p4))
