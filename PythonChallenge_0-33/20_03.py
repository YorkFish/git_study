#!/usr/bin/env python3
# coding:utf-8

from requests import get


def get_unreal(start, stop=''):
    # request
    url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
    usr_and_pwd = ("butter", "fly")
    res_range = {"Range": f"bytes={start}-{stop}"}
    res = get(url, auth=usr_and_pwd, headers=res_range)
    # response
    print("Response Status Code:", res.status_code)
    print("Content Range:", res.headers["Content-Range"])
    print("Size of Content:", len(res.content), "bytes")

    return res.content


if __name__ == "__main__":
    f = open("unreal.zip", "wb")
    f.write(get_unreal(1152983631))
    f.close()
