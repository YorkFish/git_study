#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

f = open("07_RGB.txt", 'w')
img = Image.open("oxygen.png")
pix = img.load()
for w in range(3, 609, 7):
    r, g, b, a = pix[w, 50]
    f.write(str((r, g, b, a)) + '\n')
f.close()
