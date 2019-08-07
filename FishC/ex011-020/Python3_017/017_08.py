#!/usr/bin/env python3
# coding:utf-8

from itertools import combinations		# 实现排列组合
from functools import reduce			# 全局名字空间移除了 reduce()，现在在 functools 模块里

# 偷个懒~
array = [-66, -33, 0, 99, 11, 55, 22, -44, 77, -88]

# 解法 1
print("Minimum difference is:", min([ abs(i[0]-i[1]) for i in combinations(array, 2)]))

# 解法 2
print("Minimum difference is:", reduce( lambda x,y:[y,x][x<y], [ abs(i[0]-i[1]) for i in combinations(array, 2)]))

'''
解法 1 的 combinations
for i in combinations(array, 2):
    print(i, end=' ')

>>>
(-66, -33) (-66, 0) (-66, 99) (-66, 11) (-66, 55) (-66, 22) (-66, -44) (-66, 77) (-66, -88) \
(-33, 0) (-33, 99) (-33, 11) (-33, 55) (-33, 22) (-33, -44) (-33, 77) (-33, -88) \
(0, 99) (0, 11) (0, 55) (0, 22) (0, -44) (0, 77) (0, -88) \
(99, 11) (99, 55) (99, 22) (99, -44) (99, 77) (99, -88) \
(11, 55) (11, 22) (11, -44) (11, 77) (11, -88) \
(55, 22) (55, -44) (55, 77) (55, -88) \
(22, -44) (22, 77) (22, -88) \
(-44, 77) (-44, -88) \
(77, -88)	# 我手动换了
'''

'''
解法 2 的 lambda 表达式也可以写成
lambda x, y : [x, y][x > y]

即，若 x > y，则为真，取 [x, y][1]，也就是取了 y
反之，若 x < y，则为假，取 [x, y][0]，就是取了 x
总之，是取最小值
'''

