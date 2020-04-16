#!/usr/bin/env python3
# coding:utf-8

import requests


req = requests.Session()
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 YaBrowser/16.10.0.2564 Yowser/2.5 Safari/537.36"}
url = "http://www.pythonchallenge.com/pc/hex/"
for i in range(1, 26):
    name = f"lake{i}.wav"
    res = req.get(url+name, auth=("butter", "fly"), headers=header)
    with open(r"lake\{}".format(name), "wb") as f:
        f.write(res.content)
        print(name, "has been downloaded!")
