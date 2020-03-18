#!/usr/bin/env python3
# coding:utf-8

from PIL import Image


def check_lines(filename):
    img = Image.open(filename)
    w, h = img.size
    res = []
    for h_num in range(h):
        line = []
        cnt = 1
        pix = img.getpixel((0, h_num))
        for w_num in range(1, w):
            tmp = img.getpixel((w_num, h_num))
            if tmp == pix:
                cnt += 1
            else:
                pix = tmp
                cnt = 1
            if cnt == 5:
                line.append(tmp)
                cnt = 1
        res.append(line)
    return res


if __name__ == "__main__":
    filename = "mozart.gif"
    print(check_lines(filename))
