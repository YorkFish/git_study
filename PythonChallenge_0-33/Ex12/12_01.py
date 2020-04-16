#!/usr/bin/env pyton3
# coding:utf-8

img = open("evil2.gfx", "rb")
data = img.read(80)
img.close()
array = [n for n in range(30, 40)] + [n for n in range(65, 91)] + [n for n in range(97, 123)]
for i in range(5):
    print(''.join([chr(e) for e in data[i::5] if e in array]))
