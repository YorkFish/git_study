#!/usr/bin/env python3
#coding:utf-8
class Pair(object):
    """ 存储数对 """
    def __init__(self, first, second):
        self.first = first
        self.second = second

def findPairs(arr):
    """
    键：数对的和
    值：数对
    """
    sum_pair = dict()
    len_arr = len(arr)
    
    i = 0
    while i < len_arr: # 遍历数组中所有可能的数对
        j = i + 1
        while j < len_arr: # 如果这个数对的和在 map 中没有，则放入 map 中
            sums = arr[i] + arr[j]
            if sums not in sum_pair:
                sum_pair[sums] = Pair(i, j)
            else:
                p = sum_pair[sums]
                print(f"({arr[p.first]}, {arr[p.second]}) and ({arr[i]}, {arr[j]})")
                return True
            j += 1
        i += 1
    return False

if __name__ == "__main__":
    # arr = [3, 4, 7, 10, 20, 9, 8]
    # findPairs(arr)
    arr = [3, 4, 4, 10, 20, 9, 8] # 我觉得这里有 bug，比如出现相等数字的时候
    findPairs(arr)

