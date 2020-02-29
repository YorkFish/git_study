#!/usr/bin/env python3
# coding:utf-8


# 即使 60 退休，入职期间也只有 4 年一届的闰年
def is_leap_year(year):
    return year % 4 == 0


def days_in_year(month, day):
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]  # Dec. 用不上
    return sum(months[:month]) + day


# 因为每天要写，所以全年无休
def solve(year, month, day):
    if year < 2014:
        return -1
    elif year == 2014:
        if month < 8 or (month == 8 and day < 18):
            return -1
        else:
            return days_in_year(month, day) - days_in_year(8, 17)
    else:
        res = 365 - days_in_year(8, 17)
        for y in range(2015, year):
            res += 365
            if is_leap_year(y):
                res += 1
        res += days_in_year(month, day)
        if (month == 2 and day == 29) or (month > 2 and is_leap_year(year)):
            res += 1
        return res


if __name__ == "__main__":
    print(solve(2017, 4, 19))
