#!/usr/bin/env python3
# coding:utf-8

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

res = [e.isalpha() and chr(97 + (ord(e)-97+2) % 26) or e for e in s]
print(''.join(res))
