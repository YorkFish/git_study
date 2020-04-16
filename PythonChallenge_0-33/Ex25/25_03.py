#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

filename = "lake1.wav"
f = open(filename, "rb")
data = f.read()[44:]
f.close()
img = Image.new("RGB", (60, 60))
img.frombytes(data)
img.save("lake_01.jpg")
img.close()
