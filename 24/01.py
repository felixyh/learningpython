# 使用递归编写一个十进制转换为二进制的函数（要求采用“取2取余”的方式，结果与调用bin()一样返回字符串形式）


def bin_recursion(n):
    if n == 1:
        return 1
    else:
        return str(bin_recursion(n // 2)) + str(n % 2)


print(bin_recursion(8))

# 10 / 2 = 5。。0   f(n)
# 5 / 2 = 2。。 1   f(1) + 1*2 +
# 2 /2 = 1。。0     f(a) = f(a //2 ) + (a//2)*2
# 1/2 = 0。。1 f(n)





