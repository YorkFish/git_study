#!/usr/bin/env python3
# coding:utf-8

f = open("silence.txt")
lst = []
for i in range(73):
    lst.append(len(f.readline().rstrip('\n')))
print(bytes(lst))
f.close()
