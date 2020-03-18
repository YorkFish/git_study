#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

gif = Image.open("white.gif")
frame = 0
while True:
  try:
    gif.seek(frame)
    frame += 1
    x, y, _, _ = gif.getbbox()
    print(f"({x:>3}, {y:>3})")
  except:
    break
gif.close()
