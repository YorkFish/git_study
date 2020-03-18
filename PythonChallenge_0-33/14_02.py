#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

img = Image.open("wire.png")
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # right, down, left, up
res = Image.new("RGB", [100, 100])

x, y = -1, 0
cnt = 0
d = 200
while d / 2 > 0:
    for v in delta:
        steps = d // 2
        for s in range(steps):
            x, y = x + v[0], y + v[1]
            res.putpixel((x, y), img.getpixel((cnt, 0)))
            cnt += 1
        d -= 1  # (100,) 99, 99, 98...
res.save("14_result.jpg")
