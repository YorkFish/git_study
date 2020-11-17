#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def Fibonacci(self, n):
        memo = [0] * (n + 1)

        def fib(n, memo):
            if n == 0 or memo[n]:
                return memo[n]
            if n == 1 or n == 2:
                res = 1
            else:
                res = fib(n - 1, memo) + fib(n - 2, memo)
            memo[n] = res
            return res

        return fib(n, memo)


if __name__ == "__main__":
    n = 0

    s = Solution()
    ans = s.Fibonacci(n)
    print(ans)
