# 还记得我们第一个小游戏吗？只要用户输入非整型数据，
# 程序立刻就会蹦出不和谐的异常信息然后崩溃。
# 请使用刚学的[异常处理](https://so.csdn.net/so/search?q=异常处理&spm=1001.2101.3001.7020)方法修改以下程序，提高用户体验。

import random

secret = random.randint(1, 10)
print('------------------我爱鱼C工作室------------------')
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
try:
    guess = int(temp)
except ValueError as reason:
    print('输入类型出错啦@ \n出错类型： %s' % str(reason))
    guess = secret
while guess != secret:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
print("游戏结束，不玩啦^_^")

