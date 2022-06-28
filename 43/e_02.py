# 尝试自己举例说明如何使用类的静态方法，并指出使用类的静态方法有何要点和需要注意的地方

class C:
    @staticmethod
    def show(name='felix'):
        print(name)


C.show('yang')
C.show()
c = C()
c.show()
