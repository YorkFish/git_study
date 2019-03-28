#!/usr/bin/evn python3
# coding:utf-8

# “两边夹击”
# 对 008_11.py 的改进
from math import sqrt

prime_lst = []
for i in range(101, 200, 2):		# 去掉偶数
    max_num = int(sqrt(i))			# 保险起见，可以 max_num = int(sqrt(i)) + 1
    min_num = 3						# 对奇数而言，直接从 3 开始即可
    flag = True
    while flag:
        if i % max_num == 0:
            flag = False
        elif i % min_num == 0:
            flag = False
        elif min_num >= max_num:	# 这里像是相向而行的两车碰面了
            break
        else:
            max_num -= 1			# 不确定 max_num 的奇偶性
            min_num += 2			# 对奇数而言，可排除为偶数的除数
    if flag:
        prime_lst.append(i)

print(prime_lst)
print("\nThere are {} prime numbers in total.".format(len(prime_lst)))

