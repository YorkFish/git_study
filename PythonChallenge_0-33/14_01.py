#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

img = Image.open("wire.png")
new = Image.new(img.mode, (100, 100))

i = 0
row_begin = col_begin = 0
row_end = col_end = 99
for _ in range(100*2 -1):
    for j in range(col_begin, col_end+1):
        pixel = img.getpixel((i, 0))
        new.putpixel((row_begin, j), pixel)
        i += 1
    row_begin += 1
    
    for j in range(row_begin, row_end+1):
        pixel = img.getpixel((i, 0))
        new.putpixel((j, col_end), pixel)
        i += 1
    col_end -= 1
    
    for j in range(col_end, col_begin-1, -1):
        pixel = img.getpixel((i, 0))
        new.putpixel((row_end, j), pixel)
        i += 1
    row_end -= 1
    
    for j in range(row_end, row_begin-1, -1):
        pixel = img.getpixel((i, 0))
        new.putpixel((j, col_begin), pixel)
        i += 1
    col_begin += 1

# new.show()
new.save("14_result.png")
