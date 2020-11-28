#!/usr/bin/env python3
# coding:utf-8

from hashlib import md5


def repair(data, md5str):
    n = len(data)
    for i in range(n):
        t = data[i]
        for byte in range(256):
            data[i] = byte
            if md5(data).hexdigest() == md5str:
                print("broken because of bytes", i)
                return True
        data[i] = t
    return False


if __name__ == "__main__":
    md5str = "bbb8b499a0eef99b52c7f13f4e78c24b"
    f = open("mybroken.zip", "rb")
    data = bytearray(f.read())
    f.close()

    if repair(data, md5str):
        zf = open("repaired.zip", "wb")
        zf.write(data)
        zf.close()
        print("done!")
    else:
        print("faild!")
