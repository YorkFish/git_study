#!/usr/bin/env python3
# coding:utf-8

from re import findall

with open("bodyguard.txt") as f:
    print(''.join(findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", f.read())))
