#!/usr/bin/env python3
#coding:utf-8
# 我想直接在字典中判断出 start
def printResult(inputs):
    for k in inputs.keys():
        if k not in inputs.values():
            start = k
            if start is None:
                print("unreasonable inputs")
                return
            break

    to = inputs[start]
    print(start, end=' ')
    while to:
        print(f"-> {to}", end=' ')
        start, to = to, inputs.get(to, None)
    print("over!")

if __name__ == "__main__":
    inputs = dict()
    inputs["西安"] = "成都"
    inputs["北京"] = "上海"
    inputs["大连"] = "西安"
    inputs["上海"] = "大连"
    printResult(inputs)

