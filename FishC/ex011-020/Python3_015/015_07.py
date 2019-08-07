#!/usr/bin/env python3
# coding:utf-8

# 此法权当拓展思路
def num_sum(min, max):
    tale = 0
    formula = ""
    for i in range(min, max+1, 2):
        tale += 1 / i
        formula += "1/{} + ".format(i)
    print("\n{0} = {1:.6f}".format(formula, tale))
    
    return 0

def run():
    num = int(input("Please enter a number: "))
    if num % 2 == 0:
        num_sum(2, num)
    else:
        num_sum(1, num)

if __name__ == '__main__':
    run()

