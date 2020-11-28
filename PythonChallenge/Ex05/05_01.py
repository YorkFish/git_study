#!/usr/bin/env python3
# coding:utf-8

from pickle import load

with open("banner.p", "rb") as f:
    print(load(f))
