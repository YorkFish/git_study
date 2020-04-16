#!/usr/bin/env python3
# coding:utf-8

from zipfile import ZipFile

comments = []
filename = "90052"
channel = ZipFile("channel.zip", 'r')
while filename.isdigit():
    filename += ".txt"
    f = channel.open(filename, 'r')
    line = f.readline()
    f.close()
    t = channel.getinfo(filename).comment
    comments.append(str(t, encoding="utf-8"))  # bytes -> str
    filename = bytes.decode(line.split()[-1])  # bytes -> str
print(''.join(comments))
