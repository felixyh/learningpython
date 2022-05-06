# 编写一个符合以下要求的函数：
# a. 计算打印所有参数的和乘以基数（base=3）的结果
# b. 如果参数中最后一个参数为（base=5），则设定基数为5，基数不参与求和计算

def practice1(*pram, base=3):
    return sum(pram)*base


print(practice1(1, 3, 4))
print(practice1(1, 3, 4,  base=5))
