#!/usr/bin/env python3
# coding:utf-8

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        table = set()
        for num in numbers:
            if num not in table:
                table.add(num)
            else:
                duplication[0] = num
                return True
        return False


if __name__ == "__main__":
    numbers = [2, 3, 1, 0, 2, 5, 3]
    duplication = [0]

    s = Solution()
    ans = s.duplicate(numbers, duplication)
    print(ans)
    print(duplication[0])
