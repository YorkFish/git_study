#!/usr/bin/env python3
# coding:utf-8


class Solution:
    # 返回对应char
    def __init__(self):
        self.hashMmap = {}
        self.strMemory = []

    def FirstAppearingOnce(self):
        if self.strMemory == []:
            return '#'

        for s in self.strMemory:
            if self.hashMmap[s] == 1:
                return s
        return '#'

    def Insert(self, char):
        if char == '' or char is None:
            return
        else:
            self.hashMmap[char] = self.hashMmap.get(char, 0) + 1
            self.strMemory.append(char)


if __name__ == "__main__":
    string = "go"
    # string = "google"
    # string = "googlegoogle"

    s = Solution()
    for e in string:
        s.Insert(e)
    ans = s.FirstAppearingOnce()
    print(ans)
