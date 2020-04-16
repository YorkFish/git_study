#!/usr/bin/env python3
# coding:utf-8

f = open("bodyguard.txt")
s = f.read()
f.close()

n = len(s)
res = []
target = -1
left = mid = right = 0
for i in range(n):
    if s[i].islower():
        if right == 3:
            res.append(s[target])
            target = i
            mid, right = 1, 0
        elif 0 < right < 3:
            left = mid = right = 0
        elif left == 3:
            if not mid:
                target = i
                mid = 1
            else:
                left = mid = 0
        elif left < 3:
            left = 0
    elif s[i].isupper():
        if right == 3:
            left, mid, right = -1, 0, 0
        elif 0 < right < 3:
            right += 1
        elif mid:
            right = 1
        elif left == 3:
            left = -1
        elif -1 < left < 3:
            left += 1
print(''.join(res))
