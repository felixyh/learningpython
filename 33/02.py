# input() 函数有可能产生两类异常：EOFError
# （文件末尾endoffile，当用户按下组合键 Ctrl+d 产生）和 KeyboardInterrupt（取消输入，当用户按下组合键 Ctrl+c 产生），
# 再次修改上边代码，捕获处理 input() 的两类异常，提高用户体验

import random

secret = random.randint(1, 10)
print('------------------我爱鱼C工作室------------------')
try:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
    guess = int(temp)
except (KeyboardInterrupt, EOFError) as reason:
    print('用户中断 \n原因： %s' % str(reason))
    guess = secret
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