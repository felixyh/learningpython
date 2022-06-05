# 先练练手，把我们的刚开始的那个猜数字小游戏加上界面吧?

import random
import sys

import easygui as g

g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")
secret = random.randint(1, 10)
msg = "不妨猜一下小甲鱼现在心里想的是哪个数字（1~10）："
title = "数字小游戏"
guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)

# 如果选择cancel，直接退出
if not guess:
    sys.exit()

while True:
    if guess == secret:
        g.msgbox("我草，你是小甲鱼心里的蛔虫吗？！")
        g.msgbox("哼，猜中了也没有奖励！")
        break
    else:
        if guess > secret:
            g.msgbox("哥，大了大了~~~")
        else:
            g.msgbox("嘿，小了，小了~~~")
        guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)

g.msgbox("游戏结束，不玩啦^_^")

