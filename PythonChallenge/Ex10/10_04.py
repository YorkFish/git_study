#!/usr/bin/env python3
# coding:utf-8

from functools import reduce
from itertools import groupby
from re import findall

"""
1.
>>> findall(r"(\d)(\1*)", "111221")
[('1', '11'), ('2', '2'), ('1', '')]
>>> ''.join([str(len(j)+1)+i for i, j in findall(r"(\d)(\1*)", "111221")])
'312211'

>>> x = '1'
>>> for n in range(30):
...     x=''.join([str(len(j)+1)+i for i, j in findall(r"(\d)(\1*)", x)])
... 
>>> len(x)
5808

2.
>>> [(i, list(j)) for i, j in groupby("1211")]
[('1', ['1']), ('2', ['2']), ('1', ['1', '1'])]
>>> ''.join([str(len(list(j)))+i for i, j in groupby("1211")])
'111221'

>>> x = '1'
>>> for n in range(30):
...     x = ''.join([str(len(list(j)))+i for i, j in groupby(x)])
... 
>>> len(x)
5808

3.
>>> len(reduce(lambda x, n: reduce(lambda a, b: a+str(len(list(b[1])))+b[0], groupby(x), ''), range(30), '1'))
5808
"""
