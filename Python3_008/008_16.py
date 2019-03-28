#!/usr/bin/evn python3
# coding:utf-8

lst = ([ i for i in range(100,201) if all( i%j for j in range(2,int(i**0.5)+1))])	# (*)

print(lst)
print("\nThere are {} prime numbers in total.".format(len(lst)))

'''
关于 all()，括号中所有的元素均为 true，则返回 True
此程序的 all() 中若出现 0，则返回 False

官网说，可以把 all() 看作：
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

(*) 可以这样理解
lst1 = []
for i in range(100, 201):
    lst2 = []
    for j in range(2, int(i**0.5)+1):
        lst2.append(i % j)
    if 0 not in lst2:
        lst1.append(i)
lst = lst1
'''

