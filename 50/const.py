# 问大家一个问题：Python 支持常量吗？相信很多鱼油的答案都是否定的，
# 但实际上 Python 内建的命名空间是支持一小部分常量的，
# 比如我们熟悉的 True，False，None 等，只是 Python 没有提供定义常量的直接方式而已。
# 那么这一题的要求是创建一个 const 模块，功能是让 Python 支持常量。

class Const:
    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise TypeError('常量无法改变！')
        if not name.isupper():
            raise TypeError('常量名必须由大写字母组成！')
        super().__setattr__(name, value)

#
# 细心的鱼油可能发现了，怎么我们这个 const 模块导入之后就把它当对象来使用（const.NAME = “FishC”）了呢？
# 难道模块也可以是一个对象？没错啦，在 Python 中无处不对象，到处都是你的对象。使用以下方法可以将你的模块与类 A 的对象挂钩。'''
# sys.modules 是一个字典，它包含了从 Python 开始运行起，被导入的所有模块。键就是模块名，值就是模块对象。
# '''

import sys
sys.modules[__name__] = Const()

