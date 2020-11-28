# -*- coding: utf-8 -*-

def sum15():
    """先把相加等于15的组合找出来,1~9数字不能重复出现"""
    mun_list = []
    for i in range(1, 10):
        for x in range(1, 10):
            for z in range(1, 10):
                if (i+x+z == 15) and (len({i, x, z}) == 3):
                    mun_list.append([i, x, z])
    return mun_list


def ruled_out(mun_list):
    """组合数字变成横竖斜对角都相加等于15的九宫格,组合的可能性,添加到列表中"""
    ruled_list = []
    for m1 in mun_list:
        for m2 in mun_list:
            for m3 in mun_list:
                if len(set(m1) | set(m2) | set(m3)) == 9:
                    u1 = m1[0]+m2[0]+m3[0]
                    u2 = m1[1]+m2[1]+m3[1]
                    u3 = m1[2]+m2[2]+m3[2]
                    i1 = m1[0]+m2[1]+m3[2]
                    i2 = m1[2]+m2[1]+m3[0]
                    if len({u1, u2, u3, i1, i2}) == 1:
                        # 生成了一个带格式的字符串,方便日后打印
                        ruled_list.append('\n\n%s\n%s\n%s\n\n======' % (m1, m2, m3))
    return ruled_list


# 开始工作
result_list = ruled_out(sum15())
file = open('九宫格结果.txt', 'w')
file.write('一共有%d种组合' % len(result_list))
file.writelines(result_list)
file.close()

