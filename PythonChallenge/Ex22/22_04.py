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


def get_script1(lst):
    white = 255
    side = 300
    x = y = side // 2
    img = Image.new('P', (side, side), 0)
    for dx, dy in lst:
        x += dx
        y += dy
        img.putpixel((x, y), white)
    img.show()


def get_script2(lst):
    cnt = 0
    for t in lst:
        if t == (0, 0):
            cnt += 1
    print(cnt)


def get_script3(lst):
    white = 255
    x = y = 50
    img = Image.new('P', (500, 100), 0)
    cnt = 0
    for dx, dy in lst:
        if dx == dy == 0:
            x = 50 + cnt * 100
            y = 50
            cnt += 1
        else:
            x += dx  # 这样做，每个字母都需要顺时针转 180°
            y += dy
        img.putpixel((x, y), white)
    img.show()


def get_script4(lst):
    white = 255
    x = y = 50
    img = Image.new('P', (500, 100), 0)
    cnt = 0
    for dx, dy in lst:
        if dx == dy == 0:
            x = 50 + cnt * 100
            y = 50
            cnt += 1
        else:
            x -= dx
            y -= dy
        img.putpixel((x, y), white)
    img.save("22_result.gif")


if __name__ == "__main__":
    gif = Image.open("white.gif")
    res = get_movements(gif)
    gif.close()
    get_script4(res)
