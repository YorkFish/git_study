#!/usr/bin/env python3
# coding:utf-8

f = open("up.txt")

"""
for line in f.readlines():
    if line == '\n' or line[0] == '#':
        continue
    else:
        res.append(line.rstrip().split())
"""
res = [line.rstrip().split() for line in f if line!='\n' and line[0]!='#']
dimensions = [int(e) for e in res[0]]
horizontal = [list(map(int,e)) for e in res[1:33]]
vertical = [list(map(int,e)) for e in res[33:]]

f.close()
