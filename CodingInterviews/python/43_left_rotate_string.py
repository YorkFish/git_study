#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def LeftRotateString(self, s, n):
        if s == '':
            return ''

        def myReverse(letters, start, stop):
            while start < stop:
                letters[start], letters[stop] = letters[stop], letters[start]
                start += 1
                stop -= 1

        letters = list(s)
        size = len(s)
        n = n % size
        myReverse(letters, 0, n - 1)
        myReverse(letters, n, size - 1)
        myReverse(letters, 0, size - 1)
        return ''.join(letters)


if __name__ == "__main__":
    string = "abcXYZde"
    n = 3

    s = Solution()
    ans = s.LeftRotateString(string, n)
    print(ans)
