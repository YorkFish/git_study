#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

img = Image.open("wire.png")
new = Image.new(img.mode, (100, 100))
new.putdata(img.getdata())
# new.show()
new.save("14_wrong_result.png")
