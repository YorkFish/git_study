#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def ReverseSentence(self, s):
        if s == '':
            return ''

        tmp = s.split(' ')
        tmp.reverse()
        return ' '.join(tmp)


if __name__ == "__main__":
    # string = "student. a am I"
    string = "   "

    s = Solution()
    ans = s.ReverseSentence(string)
    print(ans)
