#!/usr/bin/evn python3
# coding:utf-8

lst = [ p for p in range(101,201) if 0 not in [ p%d for d in range(2,int(p**0.5)+1)]]	# (*)

print(lst)
print("\nThere are {} prime numbers in total.".format(len(lst)))

'''
(*) 可以这样理解
lst1 = []
for p in range(101, 201):
    lst2 = []
    for d in range(2, int(p**0.5)+1):
        lst2.append(p % d)
    if 0 not in lst2:
        lst1.append(p)
lst = lst1
'''

