# property 就是一个描述符类
#
# - 自定义一个 property（MyProperty），来实现property的所有功能
# - 我们这里定义的MyProperty只是把 property的功能进行照搬，大家可以加入自己的创意

class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)


class Test:
    def __init__(self):
        self.size = 0

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size

    x = MyProperty(getSize, setSize, delSize)


test = Test()
test.x
test.x = 'x-man'
test.x
del test.x
test.x
