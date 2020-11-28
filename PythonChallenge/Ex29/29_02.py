#!/usr/bin/env python3
# coding:utf-8

from bz2 import decompress

f = open("silence.txt")
lst = []
for i in range(73):
    lst.append(len(f.readline().rstrip('\n')))
f.close()

t = bytes(lst)
print(decompress(t))
