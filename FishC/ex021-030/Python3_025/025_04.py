#!/usr/bin/env python3
# coding:utf-8


def solve(string):
    res = sorted(string, key=lambda x: ord(x) if ord(x)<97 else ord(x)-31.5)
    return ''.join(res)


if __name__ == "__main__":
    string = "easqWAwaeq"  # AaaeeqqsWw
    print(solve(string))
