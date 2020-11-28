#!/usr/bin/env python3
# coding:utf-8

f = open("evil2.gfx", "rb")
content = f.read()
f.close()
names = ["12_01.jpg", "12_02.png", "12_03.gif", "12_04.png", "12_05.jpg"]
for i in range(5):
    with open(names[i], "wb") as f:
        f.write(content[i::5])
