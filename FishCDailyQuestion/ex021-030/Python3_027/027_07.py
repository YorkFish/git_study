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
def perm(nums, stack):
    global cnt
    n = len(nums)
    if n:
        for i in range(n):
            stack.append(nums.pop(i))
            perm(nums, stack)
            nums.insert(i, stack.pop())
    else:
        if isGridView(stack):
            cnt += 1
            printGridView(stack)


if __name__ == "__main__":
    nums = [i for i in range(1, 10)]
    stack = []
    perm(nums, stack)
    print(f"There exist {cnt} methods.")
