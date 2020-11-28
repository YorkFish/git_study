#!/usr/bin/env python3
# coding:utf-8


def getCommonDivisor(m, d):
    while d:
        m, d = d, m%d
    return m


def calc(m, d):
    if d == 0:
        return "X -- ZeroDivisionError"
    elif m == 0:
        return '0'
    elif m == d:
        return '1'

    com_div = getCommonDivisor(m, d)
    return str(m//com_div) + '/' + str(d//com_div)


def myAdd(a, b, c, d):
    """ a/b + c/d """
    molecule = a*d + b*c
    denominator = b*d
    return calc(molecule, denominator)


def myMinus(a, b, c, d):
    """ a/b - c/d """
    molecule = a*d - b*c
    denominator = b*d
    return calc(molecule, denominator)


if __name__ == "__main__":
    print("1/2 + 1/3 =", myAdd(1, 2, 1, 3))
    print("1/2 + 1/0 =", myAdd(1, 2, 1, 0))
    print("1/2 + 1/2 =", myAdd(1, 2, 1, 2))

    print("1/2 - 1/3 =", myMinus(1, 2, 1, 3))
