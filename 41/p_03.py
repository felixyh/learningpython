# 定义一个类继承于 int 类型，并实现一个特殊功能：当传入的参数是字符串的时候，
# 返回该字符串中所有字符的 ASCII 码的和（使用 ord() 获得一个字符的 ASCII 码值）。
#
# 实现如下：
#
# >>> print(Nint(123))
# 123
# >>> print(Nint(1.5))
# 1
# >>> print(Nint('A'))
# 65
# >>> print(Nint('FishC'))
# 461


class Nint(int):
    def __new__(cls, arg):
        if isinstance(arg, str):
            sum_number = 0
            for each in arg:
                sum_number += ord(each)
            return int.__new__(cls, sum_number)
        else:
            return int.__new__(cls, arg)


print(Nint(123))
print(Nint(1.5))
print(Nint('A'))
print(Nint('FishC'))
