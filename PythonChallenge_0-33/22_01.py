#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

gif = Image.open("white.gif")
frame = 0
while True:
  try:
    gif.seek(frame)
    frame += 1
  except:
    break

print(frame)
gif.close()
