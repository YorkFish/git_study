#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

img = Image.open("16_mozart.gif")
h = img.histogram()
for num in h:
    if num and num % img.height == 0:
        print(h.index(num), num)
