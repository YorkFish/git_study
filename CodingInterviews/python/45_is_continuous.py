#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def IsContinuous(self, numbers):
        if numbers == []:
            return False

        numbers.sort()
        kings = numbers.count(0)
        start = kings + 1
        for i in range(start, len(numbers)):
            while numbers[i] != numbers[i - 1] + 1:
                if kings > 0:
                    numbers[i - 1] += 1
                    kings -= 1
                else:
                    return False
        return True


if __name__ == "__main__":
    numbers = [1, 0, 3, 7, 2]

    s = Solution()
    ans = s.IsContinuous(numbers)
    print(ans)
