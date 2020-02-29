#!/usr/bin/env python3
# coding:utf-8


def fadd(a, b, c, d):
    fenzi = a*d + b*c
    fenmu = b*d
    GCD = lambda x,y: x if y==0 else GCD(y, x%y)
    gcd = GCD(fenzi, fenmu)
    fenzi /= gcd
    fenmu /= gcd
    return fenzi, fenmu


def fminus(a, b, c, d):
    fenzi = a*d - b*c
    fenmu = b*d
    GCD = lambda x,y: x if y==0 else GCD(y, x%y)
    gcd = GCD(fenzi, fenmu)
    fenzi /= gcd
    fenmu /= gcd
    return fenzi, fenmu


if __name__ == "__main__":
    print('1/6 + 1/3 = %d/%d' % fadd(1, 6, 1, 3))
    print('1/2 - 1/3 = %d/%d' % fminus(1, 2, 1, 3))
