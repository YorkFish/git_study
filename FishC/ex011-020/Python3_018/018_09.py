#!/usr/bin/env python3
# coding:utf-8

# 此法权当拓展思路
# sorted()
lst1 = input("请输入一组数字，并用空格隔开： ").split()
lst2 = [ i for i in range(len(lst1))]

lst3 = list( zip(lst1, lst2))
lst3 = sorted( lst3, key=lambda lst3:lst3[1], reverse=True)

lst3 = list( map(lambda x:x[0], lst3))
print(' '.join(lst3))

'''
# 最后两句可改用下方语句
for i in lst3:
    print(i[0], end=' ')
'''

