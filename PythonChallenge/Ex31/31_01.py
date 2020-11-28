#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

left, top = 0.34, 0.57  # 0.34 + 0.57i
width, height = 0.036, 0.027
iterations = 128
img1 = Image.open("mandelbrot.gif")
w, h = img1.size
rx, ry = width/w, height/h

res = []
for y in range(h-1, -1, -1):  # 貌似 0.57 是 bottom，作者误写成了 top，故应从下往上走
    for x in range(w):
        c = complex(left + x*rx, top + y*ry)
        z = 0 + 0j
        for i in range(iterations):
            z = z*z + c
            if abs(z) > 2:
                break
        res.append(i)

img2 = img1.copy()
img2.putdata(res)
# img2.show()
img2.save("31_mandelbrot_clean.gif")  # 后几个程序将此图重命名为 newMandelbrot.gif
