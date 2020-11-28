# 只有把 5 放中间一种类型解法，并且和等于15，不过还是暴力破解看看吧

def check(a):
    """传入九宫格（列表）,判定是否破解"""
    #print("a=", a)
    if a[0]+a[1]+a[2] == a[3]+a[4]+a[5] == a[6]+a[7]+a[8]\
    == a[0]+a[3]+a[6] == a[1]+a[4]+a[7] == a[2]+a[5]+a[8]\
    == a[0]+a[4]+a[8] == a[2]+a[4]+a[6]:
        print(a)

def permute(a_list):
    """闭包处理， 保存了使用方法 for 循环和两个环境变量"""
    
    outer = []  # 记录每个九宫格排列结果
    counted = {"sudo": 0}  # 计数器
    def extract(n,i):
        """递归处理， 从列表 n 中抽一个出来，剩余的元素再排列"""
        outer.append(i)
        if len(n) == 1:
            counted['sudo'] += 1
            check(outer) 
        else:
            m = n[:]   # 复制品用于安全迭代
            m.remove(i)
            for j in m:
                extract(m, j)
        # 删去本次循环增加的 i ，保持9个元素
        outer.remove(i)
                
    for num in a_list:
        extract(a_list, num)
    print(counted)
    
a1 = [1,2,3,4,5,6,7,8,9]
permute(a1)
