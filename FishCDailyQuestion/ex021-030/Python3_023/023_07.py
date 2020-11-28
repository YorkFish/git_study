#!/usr/bin/env python3
# coding:utf-8

from tkinter import _flatten


def solve(lst):
    return list(_flatten(lst))


if __name__ == "__main__":
    list1 = [1, [2], [3, 4], [[5, 6], 7], [8, [[9, [10], 11], 12], 13]]
    print(solve(list1))
