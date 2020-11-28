#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

img = Image.open("bell.png")
_, green, _ = img.split()
data = list(green.getdata())
print(bytes([abs(i-j) for i,j in zip(data[1::2],data[::2]) if abs(i-j) != 42]))
