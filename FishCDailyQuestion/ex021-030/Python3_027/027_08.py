#!/usr/bin/env python3
# coding:utf-8


def isGridView(nums):
    s = nums[0] + nums[4] + nums[8]
    if nums[2] + nums[4] + nums[6] != s:
        return False
    for i in range(0, 9, 3):
        if nums[i] + nums[i+1] + nums[i+2] != s:
            return False
    for j in range(3):
        if nums[j] + nums[j+3] + nums[j+6] != s:
            return False
    return True


def printGridView(nums):
    for i in range(0, 9, 3):
        print(f"{nums[i]} | {nums[i+1]} | {nums[i+2]}\n-   -   -")
    print("=" * 10)


cnt = 0
def perm(nums, start=0):
    global cnt
    if start == 9 and isGridView(nums):
        cnt += 1
        printGridView(nums)
    else:
        i = start
        for j in range(start, 9):
            nums[i], nums[j] = nums[j], nums[i] 
            perm(nums, i+1)
            nums[i], nums[j] = nums[j], nums[i] 


if __name__ == "__main__":
    nums = [i for i in range(1, 10)]
    perm(nums)
    print(f"There exist {cnt} methods.")
