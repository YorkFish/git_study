#!/usr/bin/env python3
# coding:utf-8


def solve(strings):
    res = sorted(sorted(strings), key=str.upper)  # key=str.lower 也行
    return ''.join(res)


if __name__ == "__main__":
    strings = "easqWAwaeq"  # AaaeeqqsWw
    print(solve(strings))
