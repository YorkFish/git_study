#!/usr/bin/env python3
# coding:utf-8


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        len_s = len(s)
        len_p = len(pattern)
        if len_s == len_p == 0:
            return True
        elif len_s != 0 and len_p == 0:
            return False
        elif len_s == 0 and len_p != 0:
            if len_p > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])  # 不用
            else:
                return False
        else:
            if len_p > 1 and pattern[1] == '*':
                if s[0] != pattern[0] and pattern[0] != '.':
                    return self.match(s, pattern[2:])  # 不用
                else:
                    return (self.match(s, pattern[2:])  # 不用
                            or self.match(s[1:], pattern[2:])  # 用一次
                            or self.match(s[1:], pattern))  # 用 n 次
            else:
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1:], pattern[1:])  # 用一次
                else:
                    return False


if __name__ == "__main__":
    string = "aaa"
    p1 = "a.a"
    p2 = "ab*ac*a"
    p3 = "aa.a"
    p4 = "ab*a"

    s = Solution()
    print(s.match(string, p1))
    print(s.match(string, p2))
    print(s.match(string, p3))
    print(s.match(string, p4))
