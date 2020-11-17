#!/usr/bin/env python3
# coding:utf-8


class Solution:
    # s字符串
    def isNumeric(self, s):
        def isNum(string):
            symbols = ['+', '-']
            if string[0] in symbols:
                if string[1] in symbols:
                    return False
                else:
                    string = string[1:]
            if '.' not in string:
                return string.isdigit()
            else:
                lst_dot = string.split('.')
                if len(lst_dot) != 2:
                    return False
                else:
                    before = lst_dot[0] == '' or lst_dot[0].isdigit()
                    after = lst_dot[1].isdigit()
                    return before and after

        if s == '':
            return False
        elif len(s) == 1:
            return s.isdigit()
        else:
            s = s.lower()
            if 'e' not in s:
                return isNum(s)
            else:
                lst_e = s.split('e')
                if len(lst_e) != 2:
                    return False
                elif lst_e[0] == '' or lst_e[1] == '':
                    return False
                else:
                    if isNum(lst_e[1]):
                        num = eval(lst_e[1])
                    else:
                        return False
                    return isNum(lst_e[0]) and num == int(num)


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
