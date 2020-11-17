#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def StrToInt(self, s):
        if s == '':
            return 0

        string = s.strip()
        num = 0
        start = 0
        symbol = 1
        if string[0] == '+':
            start += 1
        elif string[0] == '-':
            start += 1
            symbol = -1
        for i in range(start, len(string)):
            if '0' <= string[i] <= '9':
                num = num * 10 + ord(string[i]) - 48
            else:
                return 0
        return num * symbol


if __name__ == "__main__":
    string = "  -1234  "

    s = Solution()
    ans = s.StrToInt(string)
    print(ans)
