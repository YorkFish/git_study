#!/usr/bin/env python3
# coding:utf-8

num = "1"
for i in range(30):
    cnt = 1
    t = num[0]
    s = ''
    for e in num[1:]:
        if t == e:
            cnt += 1
        else:
            s += str(cnt) + t
            cnt = 1
            t = e
    s += str(cnt) + t
    num = s
print(len(num))
