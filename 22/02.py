# 使用递归编写一个函数，利用欧几里得算法求最大公约数，例如gcd(x,y)返回值为参数x和参数y的最大公约数。


def gcder(x, y):
    if x % y == 0:
        return y
    else:
        return gcder(y, x % y)


print(gcder(9, 6))
