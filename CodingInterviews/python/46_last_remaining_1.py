#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1:
            return -1

        playing = [True] * n
        i = 0
        cnt = 0
        rest = n
        while True:
            if playing[i]:
                cnt += 1
                if cnt == (m - 1) % rest + 1:
                    cnt = 0
                    playing[i] = False
                    rest -= 1
                    if rest == 0:
                        return i
            i += 1
            if i == n:
                i = 0


if __name__ == "__main__":
    n = 10
    m = 6

    s = Solution()
    ans = s.LastRemaining_Solution(n, m)
    print(ans)
