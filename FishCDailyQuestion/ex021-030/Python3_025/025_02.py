#!/usr/bin/env python3
# coding:utf-8


def solve(string):
    res = sorted(string, key=lambda x: ord(x.lower())*2 + x.islower())
    return ''.join(res)


if __name__ == "__main__":
    string = "easqWAwaeq"  # AaaeeqqsWw
    print(solve(string))
