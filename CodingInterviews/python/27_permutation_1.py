#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def Permutation(self, ss):
        if ss == "":
            return []

        def dfs(letters, curIdx, start):
            if curIdx == size:
                res.append(''.join(temp))
                return

            for i in range(start, size):
                if mark[i] == 0:
                    mark[i] = 1
                    temp[i] = letters[curIdx]
                    if (curIdx + 1 < size and
                            letters[curIdx] != letters[curIdx + 1]):
                        dfs(letters, curIdx + 1, 0)
                    else:  # abbc
                        dfs(letters, curIdx + 1, i + 1)
                    mark[i] = 0

        size = len(ss)
        letters = sorted(ss)
        temp = [None] * size
        mark = [0] * size
        res = []
        dfs(letters, 0, 0)
        return sorted(res)


if __name__ == "__main__":
    s = Solution()
    ans = s.Permutation("abbc")
    print(ans)
