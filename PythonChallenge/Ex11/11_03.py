#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

img = Image.open("cave.jpg")
w, h = img.size
res = Image.new(img.mode, (w//2, h))
for x in range(w):
    for y in range(h):
        if not x % 2 ^ y % 2:
            res.putpixel((x//2, y), img.getpixel((x, y)))
res.show()
# res.save("11_res.png")
