#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def ReverseSentence(self, s):
        if s == '':
            return ''

        res = ''
        tmp = ''
        for c in s:
            if c != ' ':
                tmp += c
            else:
                res = tmp + ' ' + res
                tmp = ''
        res = tmp + ' ' + res
        return res[:-1]  # 牛客网不忽略末尾的空格，所以手动删除


if __name__ == "__main__":
    # string = "student. a am I"
    string = "   "

    s = Solution()
    ans = s.ReverseSentence(string)
    print(ans)
