#!/usr/bin/env python3
# coding:utf-8

from os import mkdir
from shutil import move
from pathlib import Path

addr = "D:/Filetest"
file_list = []

for afile in [ x for x in Path(addr).iterdir()]:
    file_name = afile.name                      # 若 afile: D:\Filetest1\12345-1.jpg，则 afile.name: 12345-1.jpg
    file_name_id = file_name.split('-')[0]      # 如 12345-1.jpg -> 12345

    file_addr = addr + '/' + file_name          # 路径 + 文件名
    file_addr_id = addr + '/' + file_name_id    # 路径 + 文件夹名

    if file_name_id not in file_list:
        file_list.append(file_name_id)
        mkdir(file_addr_id)
    move(file_addr, file_addr_id)
