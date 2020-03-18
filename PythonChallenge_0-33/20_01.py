#!/usr/bin/env python3
# coding:utf-8

from requests import get

# request
url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
usr_and_pwd = ("butter", "fly")
res = get(url, auth=usr_and_pwd)
# response
print("Response Status Code:", res.status_code)
print("Response Headers:", res.headers)
print("Size of Content:", len(res.content), "bytes")
print("Content:", repr(res.content[:200]))
