#!/usr/bin/env python3
# coding:utf-8


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        res = [c if c != ' ' else "%20" for c in s]
        return ''.join(res)


if __name__ == "__main__":
    string = "We Are Happy"

    s = Solution()
    ans = s.replaceSpace(string)
    print(ans)
