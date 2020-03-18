#!/usr/bin/env python3
# coding:utf-8

""" Nonogram """

from pprint import pprint
from itertools import permutations


def load_file(filename):
    f = open(filename)
    res = [line.rstrip().split() for line in f if line!='\n' and line[0]!='#']
    f.close()
    dimensions = [int(e) for e in res[0]]
    horizontal = [list(map(int,e)) for e in res[1:33]]
    vertical = [list(map(int,e)) for e in res[33:]]
    return dimensions, horizontal, vertical

    
def get_permu(line, w):
    n = len(line)
    free = w - sum(line) - (n - 1)
    res = []
    for i in range(free + 1):
        s = '0' * i + '1' * line[0]
        if n == 1:
            res.append(s + '0' * (w - len(s)))
        else:
            tails = ['0' + t for t in get_permu(line[1:], w - len(s) - 1)]
            res.extend([s + t for t in tails])
    return res


def filter_lines(lines, pos, symbol):
    f = [line for line in lines if line[pos] == symbol]
    return f


def solve():
    dimensions, horizontal, vertical = load_file("up.txt")
    width, height = dimensions
    possible = [get_permu(horizontal[i], width) for i in range(height)]
    len_poss = [len(each) for each in possible]
    # pos = [get_permu(vertical[i], height) for i in range(width)]


if __name__ == "__main__":
    # 1.
    # pprint(get_permu([10], 32))
    # print(len(get_permu([2, 6, 3, 1, 1, 1, 1, 1], 32)))  # 24310

    # 2.
    # res = get_permu([10], 32)
    # pprint(filter_lines(res, 16, '1'))

    # 3.
    solve()
