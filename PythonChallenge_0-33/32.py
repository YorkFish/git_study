#!/usr/bin/env python3
# coding:utf-8

"""
1. 获得每一行、每一列可能的所有可能
2. 针对每一行/列，寻找出相同的点
    若某一行/列所有的可能中均有某一点，则这点必是解
3. 用上一步得到点去排除其他列/行的可能
    若只有一种可能，那么这一行/列就确定了
4. 迭代 2 与 3
    若不能删至唯一，则穷举
"""


def get_data(filename):
    """ 获取大小、横/纵向组合方式 """
    f = open(filename)
    flag = -1
    size, hor, ver = [], [], []
    data = [size, hor, ver]
    for line in f:
        if line[0] == '#':
            flag += 1
        elif line[0] == '\n':
            pass
        else:
            data[flag].append(list(map(int, line.split())))
    return data


def get_candidates(nums, size):
    ''' 给出行/列的组合方式，递归地获得所有的排列，# 为选择标记 '''
    n = len(nums)
    candidates = []
    length = size - sum(nums) - (n-1)
    for i in range(length+1):
        head = ' '*i + '#'*nums[0]
        len_h = len(head)
        if n == 1:
            tail = ' ' * (size-len_h)
            candidates.append(head+tail)
        else:
            tails = [' '+j for j in get_candidates(nums[1:], size-len_h-1)]
            candidates.extend([head+tail for tail in tails])
    return candidates


def init_all_candidates(w, h, hor, ver):
    ''' 得到所有行/列的所有排列 '''
    candi_h = [get_candidates(hor[i], w) for i in range(h)]
    candi_v = [get_candidates(ver[i], h) for i in range(w)]
    return candi_h, candi_v


def filtrate(candidates, pos, symbol):
    ''' 筛选出某一行/列的符合规则的排列 '''
    if candidates == "done":
        return candidates
    return [line for line in candidates if line[pos] == symbol]


def solve(filename):
    size, hor, ver = get_data(filename)
    w, h = size[0]
    candi_h, candi_v = init_all_candidates(w, h, hor, ver)
    res = [['0']*w for _ in range(h)]
    cnt, target = 0, w*h
    while cnt < target:
        # 先针对每一行
        for row, lines in enumerate(candi_h):
            if lines == "done":
                continue
            elif len(lines) == 1:
                cnt += res[row].count('0')
                for col in range(w):
                    res[row][col] = lines[0][col]
                    candi_v[col] = filtrate(candi_v[col], row, lines[0][col])
                candi_h[row] = "done"
            else:
                for col in range(w):
                    if res[row][col] == '0':
                        for line in lines[1:]:
                            if line[col] != lines[0][col]:
                                break
                        else:
                            cnt += 1
                            res[row][col] = lines[0][col]
                            candi_v[col] = filtrate(candi_v[col], row, lines[0][col])
        # 再针对每一列
        for col, lines in enumerate(candi_v):
            if lines == "done":
                continue
            elif len(lines) == 1:
                for row in range(h):
                    if res[row][col] == '0':
                        cnt += 1
                        res[row][col] = lines[0][row]
                        candi_h[row] = filtrate(candi_h[row], col, lines[0][row])
                candi_v[col] = "done"
            else:
                for row in range(h):
                    if res[row][col] == '0':
                        for line in lines[1:]:
                            if line[row] != lines[0][row]:
                                break
                        else:
                            cnt += 1
                            res[row][col] = lines[0][row]
                            candi_h[row] = filtrate(candi_h[row], col, lines[0][row])
    return res


if __name__ == "__main__":
    res = solve("up.txt")
    new = [''.join(line)+'\n' for line in res]
    print(''.join(new))
