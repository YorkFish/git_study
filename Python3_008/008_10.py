#!/usr/bin/evn python3
# coding:utf-8

# 此法权当拓展思路
lst1=[]							# 存放非素数
lst2=[]							# 存放素数

for num in range(100, 201):
    '''若除了 1 与自身，还有自然数能凑出 num，则 num 不是素数'''
    for i in range(2, 100):		# 100 最小可换成 98
        for j in range(2, 14):	# 13^2=169, 15^2=225; max(num)=200, 169 < 200 < 225
            if i * j == num:
                lst1.append(num)
    if len(lst1) == 0:			# 若 num 是素数，则 lst1 必空
        lst2.append(num)
    lst1 = []					# 清空 lst1

print(lst2)
print("\nThere are {} prime numbers in total.".format(len(lst2)))

