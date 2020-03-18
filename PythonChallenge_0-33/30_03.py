#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

img = Image.open("30_result.png")
tmp = img.copy()
tmp = tmp.transpose(Image.ROTATE_90)
tmp = tmp.transpose(Image.FLIP_TOP_BOTTOM)
tmp.save("30_result2.png")
