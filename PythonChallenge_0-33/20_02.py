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
    print("Content:", repr(res.content[:200]))


if __name__ == "__main__":
    # get_unreal(30203)
    # get_unreal(30237)
    # get_unreal(30284)
    # get_unreal(30295)
    # get_unreal(30313)

    # get_unreal(30347)  # KeyError: 'content-range'
    
    # get_unreal(2123456788)
    # get_unreal(2123456743)
    get_unreal(1152983631)
    
    # get_unreal(1152983630)  # KeyError: 'content-range'
    # get_unreal(1153223364)  # KeyError: 'content-range'
