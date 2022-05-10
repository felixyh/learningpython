# 使用递归编写一个power()函数内建函数pow()，即power(x,y)为计算并返回x的y次幂的值。


def power(x, y):
    if y == 1:
        return x
    elif y == 0:
        return 1
    else:
        return x * power(x, y-1)


print(power(102, 10))
