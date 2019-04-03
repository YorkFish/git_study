#!/usr/bin/env python3
# coding:utf-8

# 需要读写的次数比较多
def get_num(num_lst):
    """最多只能将“元素”缩小到 2 个"""
    new_lst = []
    n = len(num_lst)

    # 为了轮回
    if n % 3 == 0:
        pass
    elif n % 3 == 1:
        new_lst.append(num_lst[-1])						# 防止看错：前面是 new_lst，后面是 num_lst
        n -= 1
    else:
        new_lst.append(num_lst[-2])
        new_lst.append(num_lst[-1])
        n -= 2

    for i in range(1, n+1):
        if i % 3 != 0:
            new_lst.append(num_lst[i-1])

    return new_lst

def run():
    n = int(input("Please enter the number of people: "))
    
    if n == 1:
        print("\nYou can't play alone.")
    elif n > 1:
        num_lst = [ i for i in range(1, n+1)]			# 1 ～ 50，数字既是元素也是“序号”
        while len(num_lst) > 2:							# 使“元素”缩小至 2 个
            num_lst = get_num(num_lst)
        print("\nThe lucky number is:", num_lst[1])		# 剩下 2 个，肯定是后者胜
    else:
        print("\nPlease enter a natural number greater than 0.")

if __name__ == '__main__':
    run()

