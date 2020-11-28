#!/usr/bin/env python3
# coding:utf-8

import os

os.chdir("D:/filetest") # 文件夹需要事先建好，这里文件夹的名字不区分大小写
for i in range(12345, 12348):
    for j in range(1, 4):
        with open("%d-%d.jpg" % (i, j), 'w'):
            pass
