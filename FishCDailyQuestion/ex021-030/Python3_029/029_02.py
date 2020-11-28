#!/usr/bin/env python3
# coding:utf-8

import fractions


def myAdd(a, b, c, d):
    # a, b 为第一个分数的分子与分母
    # c, d 为第二个分数的分子与分母
    x = fractions.Fraction(a, b)
    y = fractions.Fraction(c, d)
    print(x+y)


def myMinus(a, b, c, d):
    # a, b 为第一个分数的分子与分母
    # c, d 为第二个分数的分子与分母
    x = fractions.Fraction(a, b)
    y = fractions.Fraction(c, d)
    print(x-y)


if __name__ == "__main__":
    myAdd(1, 5, 3, 5)
    myMinus(3, 5, 1, 5)
