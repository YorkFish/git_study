#!/usr/bin/env python3
# coding:utf-8


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return "%20".join(s.split(' '))


if __name__ == "__main__":
    string = " hello"

    s = Solution()
    ans = s.replaceSpace(string)
    print(ans)
