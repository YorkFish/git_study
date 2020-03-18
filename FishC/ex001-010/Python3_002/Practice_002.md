# 1. [题源](https://fishc.com.cn/thread-84668-1-1.html)


# 2. 题目

- 企业发放的奖金根据利润提成
- 利润 (I) 低于或等于 10 万元时，奖金可提 10%
- 利润高于 10 万元，低于 20 万元时
	- 低于 10 万元的部分按 10% 提成
	- 高于 10 万元的部分，可提成 7.5%
- 20 万到 40 万之间时
	- 高于 20 万元的部分，可提成 5%
- 40 万到 60 万之间时
	- 高于 40 万元的部分，可提成 3%
- 60 万到 100 万之间时
	- 高于 60 万元的部分，可提成 1.5%
- 高于 100 万元时，超过 100 万元的部分按 1% 提成

<br>

- 从键盘输入当月利润 I，求应发放奖金总数


# 3. 分析

- 请利用数轴来分界，定位
- 注意定义时需把奖金定义成长整型

***

- 我的补充：
	- Python3 中没有 Python2 的 long，所以我用 int
