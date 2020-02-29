#!/usr/bin/env python3
# coding:utf-8


def solve(strings):
    d = {}
    for c, n in zip(range(65, 91), range(0, 52, 2)):
        d[chr(c)] = n
        d[chr(c+32)] = n+1
    return ''.join(sorted(strings, key=lambda x: d[x]))


if __name__ == "__main__":
    strings = "easqWAwaeq"  # AaaeeqqsWw
    print(solve(strings))
