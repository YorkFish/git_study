""" 版主用来抛砖引玉的 """

from random import *

robot_choice_text = ['石头','剪刀','布']
while True:   
    robot_choice = choice(robot_choice_text)
    player_choice = input('石头剪刀布（输入退出来退出程序）：')
    if player_choice not in robot_choice_text:
            print('请输入石头或剪刀或布！')
    if player_choice == robot_choice:
            print('平局啦！')
            print('机器人选择的是%s!' % (robot_choice))
    if player_choice == '石头' and robot_choice == '剪刀':
            print('你赢啦！')
            print('机器人选择的是%s!' % (robot_choice))
    elif player_choice == '石头' and robot_choice == '布':
            print('你输啦！')
            print('机器人选择的是%s!' % (robot_choice))
    if player_choice == '剪刀' and robot_choice == '布':
            print('你赢啦！')
            print('机器人选择的是%s!' % (robot_choice))
    elif player_choice == '剪刀' and robot_choice == '石头':
            print('你输啦！')
            print('机器人选择的是%s!' % (robot_choice))
    if player_choice == '布' and robot_choice == '石头':
            print('你赢啦！')
            print('机器人选择的是%s!' % (robot_choice))
    elif player_choice == '布' and robot_choice == '剪刀':
            print('你输啦！')
            print('机器人选择的是%s!' % (robot_choice))
    if player_choice == '退出':
            print('退出成功！')
            break
