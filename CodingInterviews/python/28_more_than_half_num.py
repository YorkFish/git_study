#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if numbers == []:
            return 0

        num = numbers[0]
        cnt = 1
        for i in range(1, len(numbers)):
            if cnt == 0:
                num = numbers[i]
                cnt = 1
                continue
            if num == numbers[i]:
                cnt += 1
            else:
                cnt -= 1
        return numbers.count(num) > len(numbers) // 2 and num or 0


if __name__ == "__main__":
    nums = [2, 2, 3, 2, 5, 2, 1]

    s = Solution()
    ans = s.MoreThanHalfNum_Solution(nums)
    print(ans)
