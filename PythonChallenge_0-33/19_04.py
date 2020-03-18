#!/usr/bin/env python3
# coding:utf-8

"""
with open("indian.wav", "rb") as f:
    data = f.read()
    new = open("indian_2.wav", "wb")
    file_head = data[:44]
    wave_data = data[44:]
    new.write(file_head)
    tmp = []
    for i in range(0, len(wave_data), 2):
        tmp.append(chr(wave_data[i+1]))
        tmp.append(chr(wave_data[i]))
    new.write(bytes(''.join(tmp), encoding="utf-8"))
    new.close()
"""
with open("indian.wav", "rb") as f:
    data = f.read()
    file_head = data[:44]
    wave_data = data[44:]
    tail = []
    for i in range(0, len(wave_data), 2):
        tail.extend([wave_data[i+1], wave_data[i]])
    new = open("indian_3.wav", "wb")
    new.write(file_head)
    new.write(bytes(tail))
    new.close()
