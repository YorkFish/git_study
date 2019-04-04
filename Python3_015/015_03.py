#!/usr/bin/env python3
# coding:utf-8

def num_sum(n):
    return sum([ 1/i for i in range(n, 0, -2)])

def run():
    n = int(input("Please enter the number: "))
    print("\nSum = {:.6f}".format(num_sum(n)))

if __name__ == '__main__':
    run()

