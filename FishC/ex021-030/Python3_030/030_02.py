""" 大神的方法 """

import random
list1 = ['石头', '剪刀', '布']
list2 = ['平局', '计算机赢了', '你赢了']
while True:
    computer = random.randint(0, 2)
    human = input('开始猜拳，请输入0：石头，1：剪刀，2：布。仅输入回车退出：')
    if human == '':
        break
    human = int(human)
    result = (human - computer) % 3
    print('计算机出的是%s, 你出的是%s, %s'%(list1[computer], list1[human], list2[result]))
