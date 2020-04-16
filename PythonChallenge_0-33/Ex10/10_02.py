#!/usr/bin/env python3
# coding:utf-8

num = "111221"
cnt = 4
while cnt < 30:
    n = len(num)
    c, e = 1, 0
    s = ''
    for i in range(1, n):
        if num[e] == num[i]:
            c += 1
        else:
            s += str(c) + num[e]
            c, e = 1, i
    s += str(c) + num[e]
    num = s
    cnt += 1
print(len(num))
