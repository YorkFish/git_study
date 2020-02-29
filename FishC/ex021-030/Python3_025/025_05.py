#!/usr/bin/env python3
# coding:utf-8

"""
Python2: string.letters
Python3: string.ascii_letters
"""

from string import ascii_letters as t


def solve(strings):
    res = sorted(strings, key=lambda x: [t.index(x),t.index(x)-27][t.index(x)>=26])
    return ''.join(res)


if __name__ == "__main__":
    strings = "easqWAwaeq"  # AaaeeqqsWw
    print(solve(strings))
