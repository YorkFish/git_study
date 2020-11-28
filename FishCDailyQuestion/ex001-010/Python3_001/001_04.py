#!/usr/bin/env python3
# coding:utf-8

list1 = [1,2,3,4]
set1 = set()

# update 取并集
set1.update( i*100+j*10+k for i in list1 for j in list1 for k in list1 if i!=j and j!=k and k!=i)

print(set1)
print("\n总共有 {} 种排列方式。".format(len(set1)))

