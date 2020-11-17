#!/usr/bin/env python3
# coding:utf-8


class Solution:
    # s字符串
    def isNumeric(self, s):
        s = s.strip()
        if s == '':
            return False

        idx = 0
        if s[0] == '+' or s[0] == '-':
            if len(s) > 1 and ('0' <= s[1] <= '9' or s[1] == '.'):
                idx += 1
            else:
                return False  # +, -, +x
        hasE = hasDot = False
        for i in range(idx, len(s)):
            if '0' <= s[i] <= '9':
                continue
            if s[i] == '.':
                if hasDot or hasE:
                    return False  # 123.4.5, 123e4.
                hasDot = True
            elif s[i] == 'e' or s[i] == 'E':
                if hasE or i == 0 or i == len(s) - 1:
                    return False  # 123e4e, e123, 123e
                hasE = True
            elif s[i] == '-' or s[i] == '+':
                if (s[i - 1] == 'e' or s[i - 1] == 'E') and i != len(s) - 1:
                    continue
                else:
                    return False
            else:
                return False  # 12+
        return True


if __name__ == "__main__":
    s = Solution()
    t1 = "+100"
    t2 = "5e2"
    t3 = "-123"
    t4 = "3.1416"
    t5 = "-1E-16"
    t6 = "-.123"

    f1 = "12e"
    f2 = "1a3.14"
    f3 = "1.2.3"
    f4 = "+-5"
    f5 = "12e+4.3"

    print("t1:", s.isNumeric(t1))
    print("t2:", s.isNumeric(t2))
    print("t3:", s.isNumeric(t3))
    print("t4:", s.isNumeric(t4))
    print("t5:", s.isNumeric(t5))
    print("t6:", s.isNumeric(t6))

    print("\nf1:", s.isNumeric(f1))
    print("f2:", s.isNumeric(f2))
    print("f3:", s.isNumeric(f3))
    print("f4:", s.isNumeric(f4))
    print("f5:", s.isNumeric(f5))
