#!/usr/bin/env python3
# coding:utf-8

from PIL import Image


def com_color(color):
    r, g, b = color
    return 255-r, 255-g, 255-b

if __name__ == "__main__":
    img = Image.open("19_map.jpg")
    data = map(com_color, img.getdata())
    img.putdata(list(data))
    img.save("19_new_map.jpg")
    img.close()
