#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

f = open("07_RGB2ASCII.txt", 'w')
pic = Image.open("oxygen.png")
pix = pic.load()
for w in range(3, 609, 7):  # 色块共长约 609，单个长约 7
    r, _, _, _ = pix[w, 50]  # 50 的高度必在其中
    f.write(chr(r))
f.close()
