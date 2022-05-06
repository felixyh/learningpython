# 寻找水仙花数
# 题目要求：如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。例如153 = 1^3+5^3+3^3，因此153是一个水仙花数。编写一个程序，找出所有的水仙花数。

def narcissistic():
    for i in range(100, 1000):
        x = i // 100
        y = (i // 10) % 10
        z = i % 10
        if i == pow(x, 3) + pow(y, 3) + pow(z, 3):
            print('narcissistic number: %d' % i)


narcissistic()
