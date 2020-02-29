#!/usr/bin/env python3
# coding:utf-8


def solve(lst):
    res = []
    while lst:
        tmp = lst.pop(0)
        if isinstance(tmp, list):  # type(tmp) is list; type(tmp) is int
            res.extend(solve(tmp))
        else:
            res.append(tmp)
    return res


if __name__ == "__main__":
    list1 = [1, [2], [3, 4], [[5, 6], 7], [8, [[9, [10], 11], 12], 13]]
    print(solve(list1))
