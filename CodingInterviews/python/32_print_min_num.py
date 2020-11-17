#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def PrintMinNumber(self, numbers):
        if numbers == []:
            return ''

        size = len(numbers)
        nums = list(map(str, numbers))
        for i in range(size - 1):
            flag = i
            for j in range(i + 1, size):
                if nums[j] + nums[flag] < nums[flag] + nums[j]:
                    flag = j
            if flag != i:
                nums[i], nums[flag] = nums[flag], nums[i]
        return ''.join(nums).lstrip('0') or '0'


if __name__ == "__main__":
    numbers = [3, 5, 1, 4, 2]

    s = Solution()
    ans = s.PrintMinNumber(numbers)
    print(ans)
