#!/usr/bin/env python3
# coding:utf-8

with open("indian.wav", "rb") as f:
    data = f.read()
    new = open("indian_1.wav", "wb")
    file_head = data[:44]  # 文件头部
    wave_data = data[44:]  # 声音数据
    new.write(file_head)  # 写入头部数据
    new.write(wave_data[::-1])  # 写入反转的声音数据
    new.close()
