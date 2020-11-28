#!/usr/bin/env python3
# coding:utf-8

from PIL import Image


def get_movements(f):
    ox = oy = 100
    lst = []
    for frame in range(133):
        f.seek(frame)
        x, y, _, _ = f.getbbox()
        lst.append((ox-x, oy-y))
    return lst


if __name__ == "__main__":
    gif = Image.open("white.gif")
    res = get_movements(gif)
    gif.close()

    print(list(res))
    print('=' * 30)
    print(set(res))
