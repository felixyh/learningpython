# 定义一个类 Nstr，当该类的实例对象间发生的加、减、乘、除运算时，将该对象的所有字符串的 ASCII 码之和进行计算：
# >>> a = Nstr('FishC')
# >>> b = Nstr('love')
# >>> a + b
# 899
# >>> a - b
# 23
# >>> a * b
# 201918
# >>> a / b
# 1.052511415525114
# >>> a // b
# 1

class Nstr(int):
    def __new__(cls, arg):
        sum_number = 0
        for each in arg:
            sum_number += ord(each)
        return int.__new__(cls, sum_number)


a = Nstr('FishC')
b = Nstr('love')
print(a + b)
print(a - b)
print(a * b)
print(a / b, a // b)





