#!/usr/bin/env python3
# coding:utf-8

a = ["1", "11", "21", "1211", "111221"]
cnt = 4
while cnt < 30:
    num = a[cnt]
    n = len(num)
    e = 0
    c = 1
    s = ''
    for i in range(1, n):
        if num[e] == num[i]:
            c += 1
        else:
            s += str(c) + num[e]
            e = i
            c = 1
    s += str(c) + num[e]
    a.append(s)
    cnt += 1
print(len(a[30]))
