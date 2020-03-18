#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

img = Image.open("maze.png")
dire = [(0,1), (0,-1), (1,0), (-1,0)]
entrance, exit = (639,0), (1,640)
white = (255, 255, 255, 255)
queue = [exit]
next_p = {}

while queue:
  pos = queue.pop(0)
  if pos == entrance:
    break
  for d in dire:
    temp = (pos[0]+d[0], pos[1]+d[1])
    if temp not in next_p and 0<=temp[0]<img.size[0] and 0<=temp[1]<img.size[1] and img.getpixel(temp)!=white:
      next_p[temp] = pos
      queue.append(temp)

path = []
while pos != exit:
  path.append(img.getpixel(pos)[0])
  pos = next_p[pos]
open("maze.zip", "wb").write(bytes(path[1::2]))
