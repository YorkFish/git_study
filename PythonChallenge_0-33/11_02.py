#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

img = Image.open("cave.jpg")
w, h = img.size
one = Image.new(img.mode, (w//2, h))
two = one.copy()

for x in range(w):
    for y in range(h):
        pixel = img.getpixel((x, y))
        if x % 2 == 0:
            if y % 2 == 0:
                one.putpixel((x//2, y), pixel)
            else:
                two.putpixel((x//2, y), pixel)
        else:
            if y % 2 == 0:
                two.putpixel((x//2, y), pixel)
            else:
                one.putpixel((x//2, y), pixel)
one.save("11_even.png")
two.save("11_odd.png")
