#!/usr/bin/env python3
# coding:utf-8


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        res = ''
        for c in s:
            if c == ' ':
                res += "%20"
            else:
                res += c
        return res


if __name__ == "__main__":
    string = "We Are Happy"

    s = Solution()
    ans = s.replaceSpace(string)
    print(ans)
