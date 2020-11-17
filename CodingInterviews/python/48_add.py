#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def Add(self, num1, num2):
        """
        num1 ^ num2: 不计进位的相加
        (num1 & num2) << 1: 进位
        循环至进位为零

        ~(num1 ^ 0xffffffff): 模仿 C，当 num1 为负数时，把它从无符号数转为有符号数
        C 的 int 的高位是符号位，Python 没有
        """
        while num2 != 0:
            num1, num2 =\
                (num1 ^ num2) & 0xffffffff, ((num1 & num2) << 1) & 0xffffffff
        return num1 if num1 <= 0x7fffffff else ~(num1 ^ 0xffffffff)


if __name__ == "__main__":
    num1 = 66
    num2 = 66

    s = Solution()
    ans = s.Add(num1, num2)
    print(ans)
