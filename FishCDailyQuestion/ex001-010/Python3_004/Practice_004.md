# 1. [题源](https://fishc.com.cn/thread-84717-1-1.html)


# 2. 题目

- 输入某年某月某日，判断这一天是这一年的第几天？


# 3. 分析

- 以 3 月 5 日为例
	- 先把前两个月的天数加起来
	- 然后再加上 5 天即本年的第几天

- 特殊情况
	- 闰年且输入月份大于 2 时，需多加一天

