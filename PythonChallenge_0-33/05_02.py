#!/usr/bin/env python3
# coding:utf-8

from pickle import load

with open("banner.p", "rb") as f:
    res = [''.join(i*j for i, j in line) for line in load(f)]
    print('\n'.join(res))
