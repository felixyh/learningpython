# 4个魔法方法操作属性

class C:
    # 定义当该类的属性被访问时的行为
    def __getattribute__(self, name):
        print('getattribute')
        # 仅仅测试用途，通过super函数继承默认基类的同样魔法方法，不改变魔法方法本身
        return super().__getattribute__(name)

    # 当用户试图获取一个不存在的属性的行为，如果属性存在就不会调用了; 默认行为是会报错
    def __getattr__(self, name):
        print('getattr')

    # 定义当一个属性被设置时的行为
    def __setattr__(self, name, value):
        print('setattr')
        # 仅仅测试用途，通过super函数继承默认基类的同样魔法方法，不改变魔法方法本身
        super().__setattr__(name, value)

    # 定义当一个属性被删除时的行为
    def __delattr__(self, name):
        print('delattr')
        # 仅仅测试用途，通过super函数继承默认基类的同样魔法方法，不改变魔法方法本身
        super().__delattr__(name)


c = C()
c.size
c.size = 1
c.size
del c.size
