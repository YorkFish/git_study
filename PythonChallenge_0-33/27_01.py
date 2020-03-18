#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

img = Image.open("zigzag.gif")
colors = img.getpalette()[::3]
data1 = list(img.getdata())
data2 = [colors[i] for i in data1]
data1.append(data1.pop(0))

lst = [1 for i,j in zip(data1, data2) if i!=j]
print(sum(lst))  # 9465
