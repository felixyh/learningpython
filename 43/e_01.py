# 尝试自己举一个例子说明如何使用类的静态属性。

class C:
    number = 0

    def show(self):
        return C.number


c = C()
print(c.show())
print(C.number)
