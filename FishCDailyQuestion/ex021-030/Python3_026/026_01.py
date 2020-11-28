#!/usr/bin/env python3
# coding:utf-8

from math import sqrt
from typing import List


def getPrimes(start:int, stop:int) ->List[int]:
    res = []
    if stop < 2 or stop < start:
        return -1
    elif start <= 2:
        res.append(2)
        start = 3
    elif start % 2 == 0:
        start += 1
    
    for n in range(start, stop+1, 2):
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                break
        else:
            res.append(n)
    return res


if __name__ == "__main__":
    start = 3
    stop = 3
    print(getPrimes(start, stop))
