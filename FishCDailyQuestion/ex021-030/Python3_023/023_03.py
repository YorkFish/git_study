#!/usr/bin/env python3
# coding:utf-8


def solve(lst):
    res = []
    for e in str(lst):
        if e != '[' and e != ']':
            res.append(e)
    new = '[' + ''.join(res) + ']'
    return eval(new)


if __name__ == "__main__":
    list1 = [1, [2], [3, 4], [[5, 6], 7], [8, [[9, [10], 11], 12], 13]]
    print(solve(list1))
