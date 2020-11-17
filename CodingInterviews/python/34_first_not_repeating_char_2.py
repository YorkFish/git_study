#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def FirstNotRepeatingChar(self, s):
        if s == '':
            return -1

        d1 = {}
        d2 = {}
        for c in s:
            if c not in d2:
                if c not in d1:
                    d1[c] = True
                else:
                    d2[c] = True
        for i in range(len(s)):
            if s[i] not in d2:
                return i


if __name__ == "__main__":
    string = "abcdefgabcdf"

    s = Solution()
    ans = s.FirstNotRepeatingChar(string)
    print(ans)
