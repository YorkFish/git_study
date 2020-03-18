#!/usr/bin/env python3
# coding:utf-8

s = "map"
intab = ''.join([chr(e) for e in range(97, 123)])
outtab = ''.join([chr(97 + (e-97+2) % 26) for e in range(97, 123)])
transtab = str.maketrans(intab, outtab)
print(s.translate(transtab))
