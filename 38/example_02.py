class Base1:
    def foo1(self):
        print('我代表基类 base1')


class Base2:
    def foo2(self):
        print('我代表基类 base2')


class Child(Base1, Base2):
    pass

