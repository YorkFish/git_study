#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

img1 = Image.open("mandelbrot.gif")
img2 = Image.open("newMandelbrot.gif")

diff = [(i-j) for i,j in zip(img1.getdata(), img2.getdata()) if i != j]
filterdiff = [(0, 255)[e>0] for e in diff]  # [i>0 and 255 or 0 for i in diff]
plot = Image.new('L', (23, 73))  # 'F', 'L', 'P'
plot.putdata(filterdiff)
# plot.show()
plot.save("plot.gif")
