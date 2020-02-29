#!/usr/bin/env python3
# coding:utf-8


def solve(strings):
    res = []
    for i in strings:
        if 64 < ord(i) <91:
            res.append([ord(i), i])
        elif 96 < ord(i) < 123:
            res.append([ord(i)-31.5, i])
    res.sort()
    new = ''
    for e in res:
        new += e[1]
    return new


if __name__ == "__main__":
    strings = "easqWAwaeq"  # AaaeeqqsWw
    print(solve(strings))
