#!/usr/bin/env python3
# coding:utf-8

from PIL import Image, ImageChops

img = Image.open("mozart.gif")

for y in range(img.size[1]):
    box = 0, y, img.size[0], y + 1
    row = img.crop(box)
    row_bytes = row.tobytes()
    i = row_bytes.index(195)
    row = ImageChops.offset(row, -i)  # like 'crol' in c
    img.paste(row, box)

img.save("16_result.gif")
