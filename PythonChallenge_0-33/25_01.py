#!/usr/bin/env python3
# coding:utf-8

from requests import get


def download_one(filename):
    url = "http://www.pythonchallenge.com/pc/hex/" + filename
    res = get(url, auth=("butter", "fly"))
    if res.ok:
        f = open(filename, "wb")
        f.write(res.content)
        f.close()
        return True
    else:
        return False


def download_all():
    n = 1
    while True:
        filename = f"lake{n}.wav"
        if download_one(filename):
            print(filename, "download!")
            n += 1
        else:
            print("nothing more.")
            return


if __name__ == "__main__":
    download_all()
