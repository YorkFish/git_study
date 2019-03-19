#!/usr/bin/env python3
# coding:utf-8

list1 = [ 1, 2, 3, 4]
list2 = [ i*100+j*10+k for i in list1 for j in list1 for k in list1 if i!=j and j!=k and k!=i]

print(list2)
print("\n总共有 {} 种排列方式。".format(len(list2)))

