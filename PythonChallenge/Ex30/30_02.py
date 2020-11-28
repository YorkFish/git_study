#!/usr/bin/env python3
# coding:utf-8

from PIL import Image

f = open("yankeedoodle.csv")
nums = [float(num.strip()) for num in f.read().split(',')]

img= Image.new('P', (53, 139))
img.putdata(nums, 256)
img.save("30_result.png")
