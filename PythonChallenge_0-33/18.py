#!/usr/bin/env python3
# coding:utf-8

import difflib
import gzip

data = gzip.open("deltas.gz")
left, right = [], []
for line in data:
    left.append(line[:53].decode()+"\n")  # don't forget
    right.append(line[56:].decode())

# compare = difflib.Differ().compare(left, right)
compare = difflib.ndiff(left, right)

fl = open("18_left.png", "wb")  # only in left
fb = open("18_both.png", "wb")  # both have
fr = open("18_right.png", "wb")  # only in right

for line in compare:
    bs = bytes([int(e, 16) for e in line[2:].strip().split() if e])
    if line[0] == '-':
        fl.write(bs)
    elif line[0] == '+':
        fr.write(bs)
    else:
        fb.write(bs)

fl.close()
fb.close()
fr.close()
