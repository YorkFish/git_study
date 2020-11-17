#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def FirstNotRepeatingChar(self, s):
        if s == '':
            return -1

        res = {}
        for c in s:
            res[c] = res.get(c, 0) + 1
        for i in range(len(s)):
            if res[s[i]] == 1:
                return i


if __name__ == "__main__":
    string = "abcdefgabcdf"

    s = Solution()
    ans = s.FirstNotRepeatingChar(string)
    print(ans)
