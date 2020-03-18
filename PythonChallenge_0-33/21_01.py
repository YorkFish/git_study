#!/usr/bin/env python3
# coding:utf-8

import bz2
import zlib

with open("package.pack", "rb") as f:
    data = f.read()

    while True:
        if data.startswith(b'x\x9c'):
            data = zlib.decompress(data)
        elif data.startswith(b'BZh'):
            data = bz2.decompress(data)
        elif data.endswith(b'\x9cx'):  # \x9c, x -> x, \x9c
            data = data[::-1]
        else:
            break

    print(data)  # b'sgol ruoy ta kool'
