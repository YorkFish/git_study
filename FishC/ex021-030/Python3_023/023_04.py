#!/usr/bin/env python3
# coding:utf-8


def solve(lst):
    res = [e for e in str(lst) if e not in ('[', ']')]
    return list(eval(''.join(res)))


if __name__ == "__main__":
    list1 = [1, [2], [3, 4], [[5, 6], 7], [8, [[9, [10], 11], 12], 13]]
    print(solve(list1))
