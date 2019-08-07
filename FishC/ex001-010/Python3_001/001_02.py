#!/usr/bin/env python3
# coding:utf-8

count = 0		# 记录有多少种排列方式

# i, j, k 分别表示“百位”、“十位”、“个位”
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and j != k and k != i:
                print("{}{}{}".format(i, j, k), end=', ')
                count += 1

print("\n总共有 {} 种排列方式。".format(count))

