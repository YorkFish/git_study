#!/usr/bin/env python3
# coding:utf-8

filename = "90052"
while filename.isdecimal():
    f = open(filename+".txt")
    line = f.readline()
    f.close()
    filename = line.split()[-1]
print(line)
