#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

img1 = Image.open("mandelbrot.gif")
img2 = Image.open("newMandelbrot.gif")

diff = [(i-j) for i,j in zip(img1.getdata(), img2.getdata()) if i != j]
print(len(diff))
