# 移位操作符是应用于二进制操作数的，现在需要你定义一个新的类 Nstr，也支持移位操作符的运算：
# >>> a = Nstr('I love FishC.com!')
# >>> a << 3
# 'ove FishC.com!I l'
# >>> a >> 3
# 'om!I love FishC.c'


class Nstr(str):
    def __lshift__(self, other):
        return self[other:] + self[:other]

    def __rshift__(self, other):
        return self[-other:] + self[: -other]


a = Nstr('I love FishC.com!')
print(a << 3)
print(a >> 3)
