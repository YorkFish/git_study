#!/usr/bin/env python3
# coding:utf-8

from base64 import b64decode

f = open("please.txt", "rb")
audio = open("indian.wav", "wb")

for line in f.readlines():
    audio.write(b64decode(line.strip()))

f.close()
audio.close()
