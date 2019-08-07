#!/usr/bin/env python3
# coding:utf-8

# “直角三角形”输出
for i in range(1, 10):			# i 控制行
    for j in range(1, i+1):		# j 控制列
        print("{0:} x {1:} = {2:>2}".format(j, i, i*j), end='  ')
        '''
        以下三种方式也行
		print(j, 'x', i, '=', i*j, end='  ')	# 这种写法会有一点不齐
        print('%s * %s = %2s' % (j, i, i*j), end='  ')
        print('%d * %d = %2d' % (j, i, i*j), end='  ')
        '''
    print()

