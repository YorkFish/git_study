#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

img = Image.open("cave.jpg")
small = img.crop((0, 0, 10, 5))
big = small.resize((500, 250))
big.save("11_crop_resize.png")
