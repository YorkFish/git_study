#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def FindContinuousSequence(self, tsum):
        res = []
        nums = list(range(1, (tsum + 1) // 2 + 1))
        for start in nums:
            num = tmpSum = start
            while tmpSum < tsum:
                num += 1
                tmpSum += num
                if tmpSum == tsum:
                    res.append(nums[start - 1:num])
                    break
        return res


if __name__ == "__main__":
    tsum = 3

    s = Solution()
    ans = s.FindContinuousSequence(tsum)
    print(ans)
