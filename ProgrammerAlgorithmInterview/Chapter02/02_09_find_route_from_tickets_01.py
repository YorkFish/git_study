#!/usr/bin/env python3
#coding:utf-8
def printResult(inputs):
    reverse_inputs = dict() # 用来存储把 inputs 的键与值调换后的信息
    for k,v in inputs.items():
        reverse_inputs[v] = k
    
    for k in inputs.keys():
        if k not in reverse_inputs:
            start = k
            break
    
    if start == None:
        print("unreasonable inputs")
        return

    to = inputs[start]
    while to:
        print(f"{start} -> {to},", end=' ')
        start, to = to, inputs.get(to, None)
    print("over!")

if __name__ == "__main__":
    inputs = dict()
    inputs["西安"] = "成都"
    inputs["北京"] = "上海"
    inputs["大连"] = "西安"
    inputs["上海"] = "大连"
    printResult(inputs)

