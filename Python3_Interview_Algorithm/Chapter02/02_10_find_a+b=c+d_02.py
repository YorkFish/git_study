#!/usr/bin/env python3
#coding:utf-8
def findPairs(arr):
    sum_pair = dict()
    len_arr = len(arr)
    
    for i in range(len_arr - 1):
        for j in range(i + 1, len_arr):
            sums = arr[i] + arr[j]
            if sums not in sum_pair:
                sum_pair[sums] = (i, j)
            elif i not in sum_pair[sums] and j not in sum_pair[sums]:
                t = sum_pair[sums]
                print(f"({arr[t[0]]}, {arr[t[1]]}) and ({arr[i]}, {arr[j]})")
                return True
    print("not found")
    return False

if __name__ == "__main__":
    arr1 = [3, 4, 7, 10, 20, 9, 8]
    findPairs(arr1)

    arr2 = [3, 4, 4, 10, 20, 9, 8]
    findPairs(arr2)

