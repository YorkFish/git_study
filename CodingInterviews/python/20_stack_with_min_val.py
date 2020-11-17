#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def __init__(self):
        self.stk = []
        self.store = []
    
    def push(self, node):
        self.stk.append(node)
        if self.store == []:
            self.store.append(node)
        else:
            if node < self.store[-1]:
                self.store.append(node)
            else:
                self.store.append(self.store[-1])
    
    def pop(self):
        if self.stk == []:
            return None
        self.store.pop()
        return self.stk.pop()
    
    def top(self):
        if self.stk == []:
            return None
        return self.stk[-1]
    
    def min(self):
        return self.store[-1]


if __name__ == "__main__":
    s = Solution()
    s.push(2)
    s.push(5)
    s.push(1)
    print(s.top())  # 1
    print(s.min())  # 1
    s.pop()
    print(s.top())  # 5
    print(s.min())  # 2
