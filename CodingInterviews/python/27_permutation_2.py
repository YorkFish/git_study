#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def Permutation(self, ss):
        if len(ss) < 2:
            return ss.split()

        def dfs(letters, start):
            if start == size:
                res.append(''.join(letters))
                return

            for i in range(start, size):
                if i > start and letters[i] == letters[start]:
                    continue
                letters[i], letters[start] = letters[start], letters[i]
                dfs(letters[:], start + 1)  # abbc

        size = len(ss)
        letters = sorted(ss)
        res = []
        dfs(letters, 0)
        return res


if __name__ == "__main__":
    s = Solution()
    ans = s.Permutation("abbc")
    print(ans)
