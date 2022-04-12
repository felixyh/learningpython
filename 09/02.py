# 1. 编写一个程序，求 100~999 之间的所有水仙花数。
#
# > 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。

# for number in range(100, 1000):
#     hundreds = number // 100
#     tens = (number // 10) % 10
#     single = number % 10
#
#     if number == hundreds ** 3 + tens ** 3 + single ** 3:
#         print(number, end=' ')


for number in range(100, 1000):
    numstr = str(number)
    if number == int(numstr[0])**3 + int(numstr[1])**3 + int(numstr[2])**3:
        print(number, end=' ')


