#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def InversePairs(self, data):
        # 单调不减数组没有逆序对，其余的都有
        # 给数组排序可以顺便算出逆序对
        if len(data) < 2:
            return 0

        # start    mid      stop
        # 0, 1, 2, 3, 4, 5, 6, 7
        def mergeAndCount(data, start, mid, stop, tmp):
            for i in range(start, stop + 1):
                tmp[i] = data[i]
            i = start
            j = mid + 1
            count = 0
            for k in range(start, stop + 1):
                if i == mid + 1:  # i 见底了，就用 j
                    data[k] = tmp[j]
                    j += 1
                elif j == stop + 1:  # j 见底了，就用 i
                    data[k] = tmp[i]
                    i += 1
                elif tmp[i] <= tmp[j]:
                    data[k] = tmp[i]
                    i += 1
                else:
                    data[k] = tmp[j]
                    j += 1
                    count += mid - i + 1  # [i, mid] 都能与 j 组成逆序对
            return count

        # start    mid         stop
        # 0, 1, 2, 3, 4, 5, 6, 7
        def mergeSort(data, start, stop, tmp):
            if start == stop:
                return 0
            mid = start + (stop - start) // 2
            leftPairs = mergeSort(data, start, mid, tmp)
            rightPairs = mergeSort(data, mid + 1, stop, tmp)

            if data[mid] <= data[mid + 1]:
                return leftPairs + rightPairs   

            crossPairs = mergeAndCount(data, start, mid, stop, tmp)
            return leftPairs + rightPairs + crossPairs

        tmp = [0] * len(data)
        cnt = mergeSort(data[:], 0, len(data) - 1, tmp)
        return cnt % 1000000007


if __name__ == "__main__":
    data = [8,2,3,4,5,6,7,0]

    s = Solution()
    ans = s.InversePairs(data)
    print(ans)
